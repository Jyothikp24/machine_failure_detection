# Machine Failure Prediction Using Machine Learning

## Project Overview

This project predicts potential machine failures using machine learning and sensor data. It uses machine operating parameters to estimate whether a machine is likely to experience a failure.

The project combines a machine learning model with a web interface to make predictions from user-provided inputs.

## Objectives

* Predict machine failures using sensor measurements.
* Explore machine operating conditions using data analysis.
* Build a web application for interactive predictions.
* Make the trained machine learning model accessible through an API.

## Technologies Used

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Web Framework:** FastAPI
* **Frontend:** HTML
* **API Documentation:** Swagger UI
* **Model Storage:** Joblib

## Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository.

The dataset contains 10,000 records with machine operating parameters and machine failure information.

**Dataset Link:** [AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)

### Features Used

* Machine Type
* Air Temperature (K)
* Process Temperature (K)
* Rotational Speed (rpm)
* Torque (Nm)
* Tool Wear (min)

### Target Variable

**Machine failure:** Indicates whether a machine failure occurred.

## Project Structure

```text
machine_failure_detection/
├── main.py
├── failure.joblib
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── index.html
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Jyothikp24/machine_failure_detection.git
```

### 2. Navigate to the Project Directory

```bash
cd machine_failure_detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open the Application

Open the following address in your browser:

http://127.0.0.1:8000

To access the interactive API documentation, visit:

http://127.0.0.1:8000/docs

## Machine Learning Workflow

1. Load and inspect the dataset.
2. Select relevant machine operating features.
3. Encode categorical variables.
4. Split the dataset into training and testing sets.
5. Train a machine learning classification model.
6. Evaluate the model's performance.
7. Save the trained model using Joblib.
8. Integrate the model with FastAPI.
9. Provide predictions through a web interface.

## Future Improvements

* Compare different classification algorithms.
* Evaluate model performance using precision, recall, F1-score, and a confusion matrix.
* Improve the user interface.
* Deploy the application online.

## Disclaimer

This is an educational machine learning project using a predictive maintenance dataset. Its predictions should not be treated as a substitute for professional industrial safety systems.


