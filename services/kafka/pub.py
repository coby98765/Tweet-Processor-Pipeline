from kafka import KafkaProducer
import os
import json

class Pub:
    def __init__(self,topic1,topic2):
        # self.topic_name = os.getenv("topic","")
        self.topic = f"{topic1}_tweet_{topic2}"
        self.bootstrap_servers = os.getenv("KAFKA_HOST","localhost:9092")
        self.producer = None

    def connect(self):
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")  # dict -> JSON -> bytes
            )
            print('connected to kafka')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def pub(self,data,topic):
        try:
            self.producer.send(topic,value=data)
            # print('data sent')
        except Exception as ex:
            print(ex)
            raise Exception(ex)