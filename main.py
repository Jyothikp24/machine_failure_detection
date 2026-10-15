from fastapi import FastAPI, Request, Form
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import sys
from typing import Annotated, Literal
from fastapi.templating import Jinja2Templates
from sklearn._loss import _loss as sklearn_loss

app = FastAPI()
sys.modules.setdefault("_loss", sklearn_loss)

model_data = joblib.load("failure.joblib")
model = model_data["model"]
feature_names = model_data["features"]

template = Jinja2Templates(directory="templates")


class MachineData(BaseModel):
    type: Literal["L", "M", "H"] = Field(..., description="Product quality variant")
    air_temperature: float = Field(..., description="Air temperature [K]")
    process_temperature: float = Field(..., description="Process temperature [K]")
    rotational_speed: int = Field(..., ge=0, description="Rotational speed [rpm]")
    torque: float = Field(..., ge=0, description="Torque [Nm]")
    tool_wear: int = Field(..., ge=0, description="Tool wear [min]")


@app.get("/")
async def home(request: Request):
    return template.TemplateResponse(
        request=request, name="index.html", context={"request": request}
    )


@app.post("/predict")
def predict(request: Request, data: Annotated[MachineData, Form()]):
    print("Received input:", data.model_dump())

    row = {
        "Air temperature [K]": data.air_temperature,
        "Process temperature [K]": data.process_temperature,
        "Rotational speed [rpm]": data.rotational_speed,
        "Torque [Nm]": data.torque,
        "Tool wear [min]": data.tool_wear,
        "Type_H": int(data.type == "H"),
        "Type_L": int(data.type == "L"),
        "Type_M": int(data.type == "M"),
    }

    expected = list(model.feature_names_in_)
    clean = lambda s: s.replace("[", "").replace("]", "")
    row_clean = {clean(k): v for k, v in row.items()}
    input_data = pd.DataFrame([{name: row_clean[clean(name)] for name in expected}])

    prediction = model.predict(input_data)
    print("Prediction:", prediction)

    if prediction[0] == 1:
        result = "Warning: the machine is likely to fail."
    else:
        result = "The machine is operating normally (no failure predicted)."

    return template.TemplateResponse(
        request=request, name="index.html", context={"request": request, "result": result, "inputs": data.model_dump()}
    )