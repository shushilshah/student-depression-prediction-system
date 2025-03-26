import streamlit as st
import pandas as pd
import joblib
import numpy as np
from src.pipeline.training_pipeline import TrainingPipeline
from src.utils.main_utils import save_to_mongo
from pymongo import MongoClient
from dotenv import load_dotenv
from src.components.data_transformation import DataTransformation
import os
load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION")


st.set_page_config(page_title='Predict')
st.markdown("""
    <style>
        .main {
            max-width: 100%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_model():
    model = joblib.load('model.pkl')
    return model


model = load_model()


def transform_and_predict(input_df, model):
    transformer = DataTransformation(input_df)
    transformed_input = transformer.transform()

    for col in model.feature_names_in_:
        if col not in transformed_input.columns:
            transformed_input[col] = 0

    transformed_input = transformed_input[model.feature_names_in_]

    return model.predict(transformed_input)


st.title("Depression Prediction Based on Lifestyle")

# st.markdown("Fill the form below and get prediction.")


col1, col2, col3, col4 = st.columns(4)
with col1:
    gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
    age = st.number_input("Age", min_value=12, max_value=50)
    city = st.text_input("Enter your city")
    profession = st.selectbox('Profession', ["Student", "Architect", "Teacher", "Digital Marketer", "Content Writer", "Chef",
                                             "Doctor", "Pharmacist", "Civil Engineer", "UX/UI Designer", "Educational Consultant", "Manager", "Lawyer", "Entrepreneur"])
with col2:
    academic_pressure = st.slider("Academic Pressure", 0, 5, 1)
    work_pressure = st.slider("Work Pressure (0-5)", 0, 5, 0)
    cgpa = st.number_input("CGPA (0-10)", min_value=0.0,
                           max_value=10.0, value=7.0)
    study_satisfaction = st.slider("Study Satisfaction (0-5)", 0, 5, 3)

with col3:
    job_satisfaction = st.slider("Job Satisfaction (0-5)", 0, 5, 3)
    sleep_duration = st.selectbox("Sleep Duration", [
        "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"])
    diet = st.selectbox("Diet", ["Healthy", "Moderate", "Unhealthy"])
    degree = st.selectbox(
        "Degree", ['Class 12', 'B.Ed', 'B.Com', 'B.Arch', 'BCA', 'MSc', 'B.Tech', 'MCA', 'M.Tech', 'BHM', 'BSc', 'M.Ed', 'B.Pharm', 'M.Com', 'MBBS', 'BBA', 'LLB', 'BE', 'BA', 'M.Pharm', 'MD', 'MBA', 'MA', 'PhD', 'LLM', 'MHM', 'ME', 'Others'])
with col4:
    suicidal_thoughts = st.selectbox("Suicidal Thoughts", ["Yes", "No"])
    work_study_hour = st.slider("Daily Work/Study Hours", 0.0, 16.0, 4.0)
    financial_stress = st.slider("Financial Stress (0-5)", 0, 5, 2)
    family_illness = st.selectbox("Family Illness", ['Yes', 'No'])


if st.button("Predict"):
    try:
        input_dict = {
            'Gender': gender,
            'Age': age,
            'City': city,
            'Profession': profession,
            'Academic Pressure': academic_pressure,
            'Work Pressure': work_pressure,
            'CGPA': cgpa,
            'Study Satisfaction': study_satisfaction,
            'Job Satisfaction': job_satisfaction,
            'Sleep Duration': sleep_duration,
            'Dietary Habits': diet,
            'Degree': degree,
            'Have you ever had suicidal thoughts ?': suicidal_thoughts,
            'Work/Study Hours': work_study_hour,
            'Financial Stress': financial_stress,
            'Family History of Mental Illness': family_illness

        }

        input_df = pd.DataFrame([input_dict])
        prediction = transform_and_predict(input_df, model)

        input_df['Depression'] = prediction

        save_to_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME,
                      input_df.to_dict(orient='records')[0])

        if prediction == 0:
            st.success(f"You are safe from depression.")
        else:
            st.warning(f"You are suffered from depression.")

    except Exception as e:
        st.error(f"Error during prediction: {e}")


# Optional: View history
# with st.expander("View Previous Predictions"):
#     try:
#         client = MongoClient(MONGO_URI)
#         records = list(client[DB_NAME][COLLECTION_NAME].find({}, {"_id": 0}))
#         if records:
#             df = pd.DataFrame(records)
#             st.dataframe(df)
#         else:
#             st.info("No predictions stored yet.")
#     except Exception as e:
#         st.error(f"Error loading history: {str(e)}")
