import pandas as pd
from src.logger import logging


class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            logging.info(f"Starting data ingestion from {self.file_path}")
            data = pd.read_csv(self.file_path)
            logging.info(
                f"Data ingested successfully! Loaded {data.shape[0]} rows and {data.shape[1]} columns.")
            return data

        except Exception as e:
            logging.error(f"Error during data ingestion: {e}")
            raise e
