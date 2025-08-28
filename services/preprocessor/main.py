from services.kafka.pub import Pub
from services.kafka.sub import Sub
from manager import Manager
import os

TOPIC = os.getenv("TOPIC", "antisemitic")
sub_topic = f"raw_tweets_{TOPIC}"
pub_topic = f"preprocessed_tweets_{TOPIC}"

#Kafka publisher
publisher = Pub("preprocessor")
publisher.connect()

#Kafka subscriber
subscriber = Sub(sub_topic)
subscriber.connect()
if __name__ == '__main__':
    manager = Manager(subscriber, publisher, pub_topic)
    manager.run()