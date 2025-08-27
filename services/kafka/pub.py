from kafka import KafkaProducer
import os

class Pub:
    def __init__(self,topic,bootstrap_servers):
        self.topic_name = os.getenv(topic)
        self.bootstrap_servers = os.getenv(bootstrap_servers)
        self.producer = None

    def connect(self):
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
            print('connected to kafka')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def pub(self,data):
        try:
            self.producer.send(self.topic_name,data)
            print('data sent')
        except Exception as ex:
            print(ex)
            raise Exception(ex)