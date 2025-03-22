import pandas as pd
from src.logger import logging
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
# class DataIngestion:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def load_data(self):
#         try:
#             logging.info(f"Starting data ingestion from {self.file_path}")
#             data = pd.read_csv(self.file_path)
#             logging.info(
#                 f"Data ingested successfully! Loaded {data.shape[0]} rows and {data.shape[1]} columns.")
#             return data

#         except Exception as e:
#             logging.error(f"Error during data ingestion: {e}")
#             raise e


class DataIngestion:
    def __init__(self, db_name, collection_name, mongo_uri=None):
        self.mongo_uri = mongo_uri or os.getenv("MONGO_URI")
        self.db_name = db_name
        self.collection_name = collection_name

    def load_data(self):
        try:
            logging.info(f"Connecting to MongoDB at {self.mongo_uri}")
            client = MongoClient(self.mongo_uri)
            db = client[self.db_name]
            collection = db[self.collection_name]

            logging.info(
                f"Fetching data from {self.collection_name} collection in {self.db_name} database.")
            data = list(collection.find())
            df = pd.DataFrame(data)

            if '_id' in df.columns:
                df.drop(columns=['_id'], inplace=True)

            logging.info(
                f"Data ingested successfully from MongoDB! Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
            return df

        except Exception as e:
            logging.error(f"Error during MongoDB Data ingestion: {e}")
            raise e
