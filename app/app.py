import streamlit as st
import pickle
import os
import pandas as pd


try:
    model_path = '../models/'
    model_filename = os.path.join(model_path, 'model_pipeline.pkl')
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except FileNotFoundError:
    st.error("Model file not found.")


st.title("Heart Disease Prediction App")
st.write("This app predicts the presence of heart disease based on user inputs.")

# User input fields
age      = st.number_input("Age", min_value=10, max_value=100, value=25)
sex      = st.selectbox("Sex", options=["Male", "Female"])
cp       = st.selectbox("Chest Pain Type", options=[1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure", min_value=90, max_value=200, value=120)
chol     = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs      = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
restecg  = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2])
thalach  = st.number_input("Maximum Heart Rate Achieved", min_value=70, max_value=210, value=150)
exang    = st.selectbox("Exercise Induced Angina", options=[0, 1])
oldpeak  = st.number_input("Oldpeak", min_value=0.0, max_value=6.5, value=2.0)
slope    = st.selectbox("Slope", options=[1, 2, 3])
ca       = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3])
thal     = st.selectbox("Thalassemia", options=[3, 6, 7])


if st.button("Predict"):
    try:
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        input_data = pd.DataFrame([input_data], columns=feature_names)
        
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0][1]

        if not prediction:
            st.balloons()
            st.success("Congratulations! You are not at risk of heart disease.")
        else:
            st.error("Unfortunately, you are at risk of heart disease.")
            st.write("Prediction: **Heart Disease**")
        st.write(f"Prediction Probability: **{prediction_proba * 100:.2f}%**")

    except Exception as e:
        st.error("Error occurred during prediction.")
