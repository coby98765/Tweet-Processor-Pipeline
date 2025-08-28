from services.kafka.sub import Sub
from dal import Loader
import os

TOPIC = os.getenv("TOPIC", "antisemitic")
sub_topic = f"enriched_preprocessed_tweets_{TOPIC}"


#Kafka subscriber
subscriber = Sub(sub_topic)
subscriber.connect()

dal = Loader()
if __name__ == '__main__':
    for tweet in subscriber.sub():
        print(tweet)
        tweet_id = dal.load_to_mongodb(tweet,TOPIC)
        print(tweet_id)
