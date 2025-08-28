from services.kafka.sub import Sub
from enrich import DataProcessing
from services.kafka.pub import Pub
import os

TOPIC = os.getenv("TOPIC", "antisemitic")
sub_topic = f"preprocessed_tweets_{TOPIC}"
pub_topic = f"enriched_preprocessed_tweets_{TOPIC}"

#Kafka publisher
publisher = Pub("enricher")
publisher.connect()

#Kafka subscriber
subscriber = Sub(sub_topic)
subscriber.connect()

enrich = DataProcessing()
if __name__ == '__main__':
    for tweet in subscriber.sub():
        print(tweet)
        enriched_tweet = enrich.tweets_info(tweet)
        publisher.pub(enriched_tweet,pub_topic)
