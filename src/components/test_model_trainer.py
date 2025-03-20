import pandas as pd
from src.components.model_trainer import ModelTrainer
from src.components.data_transformation import DataTransformation


data = pd.read_csv('data\student_depression_dataset.csv')

transform = DataTransformation(data)
transform_data = transform.transform()


trainer = ModelTrainer(transform_data)

accuracy, report = trainer.train_model()

print("Model Acccuracy: ", accuracy)
print("Classification Report: ", report)
