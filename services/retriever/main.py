from dal import DAL
from utils import Utils
from services.kafka.pub import Pub
import time

#DAL
dal = DAL()
data = dal.get_data()
#Kafka
publisher = Pub("raw")
publisher.connect()

if __name__ == "__main__":
    counter = 0
    while True:
        data = dal.get_data(count=counter)
        tweets = Utils.normalize_objects(data)
        for tweet in tweets:
            if tweet["Antisemitic"]:
                publisher.pub(tweet, "raw_tweets_antisemitic")
            else:
                publisher.pub(tweet, "raw_tweets_non_antisemitic")
        counter += 1
        time.sleep(60)
