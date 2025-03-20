import pandas as pd
from src.components.data_transformation import DataTransformation

data = pd.read_csv('data\student_depression_dataset.csv')

# Apply transformation

transform = DataTransformation(data)
transformed_data = transform.transform()

print("Transformed data: ", transformed_data)
