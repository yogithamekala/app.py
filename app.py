# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LFClt-KTULOAPjNOoM57UFJbZ_COos2F
"""

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Create a synthetic employee attrition dataset
np.random.seed(42)
data_size = 1000
data = {
    'Age': np.random.randint(20, 60, size=data_size),
    'DistanceFromHome': np.random.randint(1, 30, size=data_size),
    'YearsAtCompany': np.random.randint(1, 20, size=data_size),
    'JobSatisfaction': np.random.randint(1, 5, size=data_size),
    'Attrition': np.random.choice([0, 1], size=data_size, p=[0.7, 0.3])  # 30% attrition
}

df = pd.DataFrame(data)

# Features and target variable
X = df.drop('Attrition', axis=1)
y = df['Attrition']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Save the model and scaler
joblib.dump(model, 'attrition_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

import streamlit as st
import joblib
import pandas as pd

# Load the trained model and scaler
model = joblib.load('attrition_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app
st.title("Employee Attrition Risk Prediction")

# Create input fields for user input
age = st.number_input("Age", min_value=20, max_value=60, value=30)
distance_from_home = st.number_input("Distance from Home (miles)", min_value=1, max_value=30, value=5)
years_at_company = st.number_input("Years at Company", min_value=1, max_value=20, value=5)
job_satisfaction = st.selectbox("Job Satisfaction", options=[1, 2, 3, 4])

# Prepare the input data
input_data = pd.DataFrame({
    'Age': [age],
    'DistanceFromHome': [distance_from_home],
    'YearsAtCompany': [years_at_company],
    'JobSatisfaction': [job_satisfaction]
})

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Make predictions
if st.button("Predict Attrition Risk"):
    prediction = model.predict(input_data_scaled)
    risk = "High Risk of Attrition" if prediction[0] == 1 else "Low Risk of Attrition"
    st.write(f"Prediction: {risk}")

# Specify your required packages
requirements = """
streamlit
scikit-learn
pandas
joblib
"""

# Write the requirements to a text file
with open("requirements.txt", "w") as f:
    f.write(requirements.strip())