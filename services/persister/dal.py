from pymongo import MongoClient

class Loader:
    @staticmethod
    def load_to_mongodb(host,db_name,collection,massage):
        try:
            client = MongoClient(host)
            mydb = client[db_name]
            collection = mydb[collection]
            res = collection.insert_one(massage)
            return res.inserted_id
        except Exception as ex:
            print(ex)
            raise Exception(ex)