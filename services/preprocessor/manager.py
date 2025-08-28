from processor import Processor


class Manager:
    def __init__(self, subscriber, publisher,out_topic):
        self.subscriber = subscriber
        self.publisher = publisher
        self.pub_topic = out_topic

    def run(self):
        for tweet in self.subscriber.sub():
            tweet["clean_text"] = Processor.run(tweet["original_text"])
            self.publisher.pub(tweet,self.pub_topic)