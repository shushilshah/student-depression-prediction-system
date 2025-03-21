import joblib
from sklearn.metrics import accuracy_score, classification_report
from src.logger import logging
import pandas as pd
import numpy as np


class ModelEvaluation:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        try:
            logging.info(f"Loading trained model from model.pkl ")
            self.model = joblib.load('model.pkl')
            logging.info("Model Loaded successfully.")

        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise Exception(f"Model load error: {e}")

    def evaluate_model(self):
        try:
            if len(self.X_test.shape) == 1:
                self.X_test = self.X_test.reshape(-1, 1)

            logging.info("Starting model evaluation.")

            y_pred = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            report = classification_report(self.y_test, y_pred)

            logging.info(f"Model Accuracy: {accuracy:.4f}")
            logging.info(f"Classification report: {report}")

            logging.info("Model evaluation completed successfully.")
            return accuracy, report

        except Exception as e:
            logging.error(f"Error during model evaluation: {e}")
            raise Exception(f"Model Evaluation error: {e}")
