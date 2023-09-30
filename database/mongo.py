import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class MongoDB:
    def __init__(self):
        self.mongo_uri = os.getenv('MONGO_URI')
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client.get_database()

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()