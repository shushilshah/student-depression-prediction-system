import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("data\student_depression_dataset.csv")

# connect to MongoDB

client = MongoClient(
    "mongodb+srv://shushil:admin123@cluster0.y6vd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["student_depression_prediction_db"]
collection = db['depression_data']

# Inserting data
collection.delete_many({})
collection.insert_many(df.to_dict(orient='records'))

print("Data inserted into MongoDB successfully.")
