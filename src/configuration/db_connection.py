import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")

df = pd.read_csv("data\student_depression_dataset.csv")

# connect to MongoDB

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

# Inserting data
collection.delete_many({})
collection.insert_many(df.to_dict(orient='records'))

print("Data inserted into MongoDB successfully.")
