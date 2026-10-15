\# Machine Failure Prediction Using Machine Learning



\## Project Overview



This project predicts potential machine failures using machine learning and sensor data. It uses machine operating parameters to estimate whether a machine is likely to experience a failure.



The project combines a machine learning model with a web interface to make predictions from user-provided inputs.



\## Objectives



\* Predict machine failures using sensor measurements.

\* Explore machine operating conditions using data analysis.

\* Build a web application for interactive predictions.

\* Make the trained machine learning model accessible through an API.



\## Technologies Used



\* \*\*Programming Language:\*\* Python

\* \*\*Machine Learning:\*\* Scikit-learn

\* \*\*Data Processing:\*\* Pandas, NumPy

\* \*\*Web Framework:\*\* FastAPI

\* \*\*Frontend:\*\* HTML

\* \*\*API Documentation:\*\* Swagger UI

\* \*\*Model Storage:\*\* Joblib



\## Dataset



This project uses the AI4I 2020 Predictive Maintenance Dataset from the UCI Machine Learning Repository.



The dataset contains 10,000 records with machine operating parameters and machine failure information.



Dataset Link:

AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository



The dataset contains machine operating measurements, including:



\* Air temperature

\* Process temperature

\* Rotational speed

\* Torque

\* Tool wear

\* Machine type



\*\*Target variable:\*\* `Machine failure`



The target indicates whether a machine failure occurred.



\## Project Structure



```text

machine-failure-prediction/

│

├── main.py

├── failure.joblib

├── requirements.txt

├── README.md

├── .gitignore

│

└── templates/

&#x20;   └── index.html

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



Replace `YOUR\_GITHUB\_REPOSITORY\_URL` with your repository's actual URL.



\### 2. Navigate to the project directory



```bash

cd machine-failure-prediction

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



On Windows:



```bash

venv\\Scripts\\activate

```



\### 5. Install the dependencies



```bash

pip install -r requirements.txt

```



\### 6. Run the application



```bash

uvicorn main:app --reload

```



\### 7. Open the application



Open the local address displayed in your terminal.



To access the interactive API documentation, visit:



```text

http://127.0.0.1:8000/docs

```



\## Machine Learning Workflow



1\. Load and inspect the dataset.

2\. Select relevant machine operating features.

3\. Encode categorical variables.

4\. Split the dataset into training and testing sets.

5\. Train a Logistic Regression model.

6\. Evaluate the model's performance.

7\. Save the trained model.

8\. Integrate the model with FastAPI.

9\. Provide predictions through a web interface.



\## Future Improvements



\* Compare Logistic Regression with Random Forest and other classification algorithms.

\* Improve failure detection using precision, recall, and F1-score.

\* Enhance the user interface.

\* Deploy the application online.



\## Disclaimer



This is an educational machine learning project using a predictive maintenance dataset. Its predictions should not be treated as a substitute for professional industrial safety systems.



