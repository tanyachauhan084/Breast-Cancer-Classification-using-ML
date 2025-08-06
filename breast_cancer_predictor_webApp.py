# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 21:23:12 2025

@author: Admin
"""

import streamlit as st
import pickle
import numpy as np

# Load your trained logistic regression model
with open("Logistic_model.pkl", "rb") as file:
    pickle.load(file)
    

# Streamlit app title and description
st.title("🔬 Breast Cancer Prediction App")
st.write("Enter the following features to predict if the tumor is **Benign (0)** or **Malignant (1)**.")

# Define all 30 input features
feature_names = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
    'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

# Input form for all features
input_data = []
with st.form("prediction_form"):
    for feature in feature_names:
        value = st.number_input(f"{feature}", min_value=0.0, step=0.01, format="%.4f")
        input_data.append(value)
    
    submitted = st.form_submit_button("Predict")

# Predict and display result
if submitted:
    prediction = model.predict([input_data])
    result = "🟢 Benign (0)" if prediction[0] == 0 else "🔴 Malignant (1)"
    st.success(f"🎯 Prediction: {result}")
