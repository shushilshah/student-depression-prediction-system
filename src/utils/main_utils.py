from pymongo import MongoClient


def save_to_mongo(uri, db_name, collection_name, record):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(record)
    client.close()
