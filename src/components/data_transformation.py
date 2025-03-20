import pandas as pd
import numpy as np
from src.logger import logging


class DataTransformation:
    def __init__(self, data):
        self.data = data

    def transform(self):
        try:
            logging.info(f"Starting data trasnformation.")

            self.data = self.data.rename(columns={
                'Gender': 'gender',
                'Age': 'age',
                'City': 'city',
                'Profession': 'profession',
                'Academic Pressure': 'academic_pressure',
                'Work Pressure': 'work_pressure',
                'CGPA': 'cgpa',
                'Study Satisfaction': 'study_satisfaction',
                'Job Satisfaction': 'job_satisfaction',
                'Sleep Duration': 'sleep_duration',
                'Dietary Habits': 'diet',
                'Degree': 'degree',
                'Have you ever had suicidal thoughts ?': 'suicidal_thoughts',
                'Work/Study Hours': 'work_study_hour',
                'Financial Stress': 'financial_stress',
                'Family History of Mental Illness': 'family_illness'
            })

            logging.info("Renamed columns.")

            self.data = self.data.drop(
                columns=['id', 'work_pressure', 'sleep_duration'], axis=1)
            logging.info("Unnecessary columns are dropped.")

            city_counts = self.data['city'].value_counts()
            self.data['city'] = self.data['city'].apply(
                lambda x: 'Other' if city_counts[x] < 5 else x)
            logging.info("Replaced less frequent city names with 'Other'.")

            self.data = pd.get_dummies(self.data, columns=[
                                       'gender', 'profession', 'diet', 'suicidal_thoughts', 'family_illness'], drop_first=True)
            logging.info("Applied one hot encoding on categorical features.")

            self.data = self.data[self.data['financial_stress'] != '?']
            logging.info("Removed rows with '?' in financial stress columns.")

            self.data['financial_stress'] = self.data['financial_stress'].astype(
                float).astype(int)
            logging.info('Converted financial data into integer value.')

            logging.info('Data transformation step completed successfully.')
            return self.data

        except Exception as e:
            logging.info(f"Error during data transformation: {e}")
            raise Exception(f"Data transformation error: {e}")
