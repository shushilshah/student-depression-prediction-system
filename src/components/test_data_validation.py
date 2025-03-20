from src.components.data_validation import DataValidation
from src.logger import logging
import pandas as pd

data = pd.read_csv("data\student_depression_dataset.csv")

validator = DataValidation(data)

validated_data = validator.validate()

print("Cleaned data:", validated_data)
