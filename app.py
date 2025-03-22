import streamlit as st
import pandas as pd
import joblib
import numpy as np
from src.components.data_transformation import DataTransformation

model = joblib.load('model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

st.set_page_config(page_title="Depression Prediction App", layout="centered")
st.title("Depression Prediction Based on Lifestyle")

with st.form("input_form"):
    st.subheader("Enter the Information:")

    gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
    age = st.number_input("Age", min_value=12, max_value=50)
    profession = st.selectbox('Profession', ["Student", "Architect", "Teacher", "Digital Marketer", "Content Writer", "Chef",
                              "Doctor", "Pharmacist", "Civil Engineer", "UX/UI Designer", "Educational Consultant", "Manager", "Lawyer", "Entrepreneur"])
    academic_pressure = st.slider("Academic Pressure", 0, 5, 1)
    work_pressure = st.slider("Work Pressure (0-5)", 0, 5, 0)
    cgpa = st.number_input("CGPA (0-10)", min_value=0.0,
                           max_value=10.0, value=7.0)
    study_satisfaction = st.slider("Study Satisfaction (0-5)", 0, 5, 3)
    job_satisfaction = st.slider("Job Satisfaction (0-5)", 0, 5, 3)
    sleep_duration = st.selectbox("Sleep Duration", [
                                  "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"])
    diet = st.selectbox("Diet", ["Healthy", "Moderate", "Unhealthy"])
    degree = st.selectbox(
        "Degree", ["BCA", "BSc", "BA", "B.Pharm", "M.Tech", "Other"])
    suicidal_thoughts = st.selectbox("Suicidal Thoughts", ["Yes", "No"])
    work_study_hour = st.slider("Daily Work/Study Hours", 0.0, 16.0, 4.0)
    financial_stress = st.slider("Financial Stress (0-5)", 0, 5, 2)
    family_illness = st.selectbox("Family Illness", ["Yes", "No"])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_dict = {
        'gender': gender,
        'age': age,
        # 'city': city,
        'profession': profession,
        'academic_pressure': academic_pressure,
        'work_pressure': work_pressure,
        'cgpa': cgpa,
        'study_satisfaction': study_satisfaction,
        'job_satisfaction': job_satisfaction,
        'sleep_duration': sleep_duration,
        'diet': diet,
        'degree': degree,
        'suicidal_thoughts': suicidal_thoughts,
        'work_study_hour': work_study_hour,
        'financial_stress': financial_stress,
        'family_illness': family_illness

    }

    input_df = pd.DataFrame([input_dict])

    try:
        transformed_input = DataTransformation(input_df)
        prediction = model.predict(transformed_input)

        if prediction[0] == 1:
            st.error("You are in depression...")
        else:
            st.success("You are safe from depression...")

    except Exception as e:
        st.error(f"Error in prediction: {e}")
