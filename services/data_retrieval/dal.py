from pymongo import MongoClient ,errors
import os

class DAL:
    def __init__(self):
        self.client = None
        self.DB_HOST = os.getenv("DB_HOST", "mongodb://localhost:27017/")
        self.DB_NAME = os.getenv("DB_NAME", "Tweets")

    def get_all(self, coll_name):
        try:
            self.client = MongoClient(self.DB_HOST)
            mydb = self.client[self.DB_NAME]
            collection = mydb[coll_name]
            res = collection.find()
            return res
        except errors.ServerSelectionTimeoutError as err:
            print(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            print(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            print(f"Configuration error: {err}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise