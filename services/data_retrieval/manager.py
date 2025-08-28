from dal import DAL
class Manager:
    def __init__(self):
        self.dal = DAL()

    def run(self,coll):
        res = self.dal.get_all(coll)
        normalized = Manager.normalize_objects(res)
        return normalized

    @staticmethod
    def normalize_objects(tweet_list):
        for tweet in tweet_list:
            x = tweet.pop('_id')
        return tweet_list
