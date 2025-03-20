import pandas as pd
from src.logger import logging


class DataValidation:
    def __init__(self, data):
        self.data = data

    def validate(self):
        try:
            logging.info(
                f"Checking the missing values present in the dataset.")
            missing_values = self.data.isnull().sum()
            if missing_values.sum() == 0:
                logging.info(f"No missing values found in the dataset.")
                print("there is no any missing values.")
            else:
                logging.warning(f"Missing value present in the dataset.")
                print("Missing values detected:\n", missing_values)
                return missing_values

            logging.info("Checking for duplicate rows.")
            duplicate_rows = self.data.duplicated().sum()
            if duplicate_rows > 0:
                logging.warning(
                    f"Found {duplicate_rows} duplicate rows. Removing them.")
                self.data = self.data.drop_duplicates()
                print(f"Removed {duplicate_rows} duplicate rows.")

            else:
                logging.info("No duplicate rows found.")
                print("No duplicate record found.")

            return self.data

        except Exception as e:
            logging.error(f"Error during data validation: {e}")
            raise Exception(f"Data validation error: {e}")
