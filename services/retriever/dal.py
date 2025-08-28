from bson import ObjectId
from pymongo import MongoClient ,errors
import os


class DAL:
    def __init__(self):
        self.client = None
        self.DB_HOST = os.getenv("DB_HOST","cluster0.6ycjkak.mongodb.net")
        self.DB_NAME = os.getenv("DB_NAME","IranMalDB")
        self.DB_COLL = os.getenv("DB_COLL","tweets")
        DB_USER = os.getenv("DB_USER","IRGC_NEW")
        DB_PASS = os.getenv("DB_PASS","iran135")
        self.limit = 100
        self.db_url = f"mongodb+srv://{DB_USER}:{DB_PASS}@{self.DB_HOST.lower()}/"

    def connect(self):
        try:
            self.client = MongoClient(self.db_url)
            self.client.admin.command("ping")
            print(f"Connected to {self.DB_NAME}!")
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

    def close_conn(self):
        self.client.close()

    def get_data(self,count=0):
        try:
            self.connect()
            db = self.client[self.DB_NAME]
            collection = db[self.DB_COLL]
            result = list(collection.find({})\
                          .sort("CreateDate", 1)\
                          .skip(self.limit * count)\
                          .limit(self.limit))
            return result
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()