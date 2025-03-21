import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from sklearn.model_selection import train_test_split
from src.logger import logging
import joblib


class TrainingPipeline:
    def __init__(self, data_path):
        self.data_path = data_path

    def run_pipeline(self):
        try:
            logging.info(
                "Starting the training pipeline.........................")

            logging.info("Loading data.......")

            ingestion = DataIngestion(self.data_path)
            data = ingestion.load_data()

            logging.info(
                "Validating the dataset for transformation.......................")

            validator = DataValidation(data)
            missing_values = validator.validate()

            if missing_values is None:
                logging.warning(
                    "Missing values detected! Handle the missing values first....................")

            logging.info("Transforming data.......")
            transform = DataTransformation(missing_values)
            transformed_data = transform.transform()

            logging.info("Training the model...........")
            trainer = ModelTrainer(transformed_data)
            X_test, y_test, accuracy, report = trainer.train_model()

            logging.info(f"Evaluating model.........")
            evaluator = ModelEvaluation(None, X_test, y_test)
            accuracy, report = evaluator.evaluate_model()

            # logging.info(f"Model accuracy: {accuracy:.4f}")
            # logging.info(f"Classification report: {report}")

            logging.info("Training pipeline completed successfully! ")
            return accuracy, report

        except Exception as e:
            logging.error(f"Error in training pipeline: {e}")
            raise e
