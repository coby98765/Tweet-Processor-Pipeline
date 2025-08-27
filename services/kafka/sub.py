from kafka import KafkaConsumer
import os

class Sub:
    def __init__(self,topic,bootstrap_servers,group):
        self.topic_name = os.getenv(topic)
        self.topic = f"{"Enter here"}_tweets_{self.topic_name}"
        self.bootstrap_servers = os.getenv(bootstrap_servers)
        self.group_id = os.getenv(group)
        self.consumer = None

    def connect(self):
        try:
            self.consumer = KafkaConsumer(
                self.topic_name,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id
                )
            print('connected to kafka')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def sub(self):
        try:
            massages = []
            for msg in self.consumer:
                massages.append(msg)
            print('data received')
            return massages
        except Exception as ex:
            print(ex)
            raise Exception(ex)