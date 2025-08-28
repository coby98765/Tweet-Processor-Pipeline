from services.kafka.sub import Sub
from enrich import DataProcessing
from services.kafka.pub import Pub

if __name__=='__main__':
    sub1 = Sub()
    sub2 = Sub()
    sub1.connect()
    sub2.connect()
    processing1 = DataProcessing(sub1.sub())
    processing2 = DataProcessing(sub2.sub())
    pub1 = Pub('','')
    pub2 = Pub('','')
    pub1.connect()
    pub2.connect()
    pub1.pub(processing1,'enriched_preprocessed_tweets_antisemitic')
    pub2.pub(processing2,'enriched_preprocessed_tweets_not_antisemitic')
