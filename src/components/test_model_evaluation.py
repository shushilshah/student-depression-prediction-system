import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_evaluation import ModelEvaluation
import joblib
data = pd.read_csv('data\student_depression_dataset.csv')

transform = DataTransformation(data)
transform_data = transform.transform()

X = transform_data.drop(columns=['depression'])
y = transform_data['depression']
model = joblib.load('model.pkl')
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

evaluator = ModelEvaluation(model, X_test, y_test)
accuracy, report = evaluator.evaluate_model()

print("The model accuracy :", accuracy)
print("Classification Report: ", report)
