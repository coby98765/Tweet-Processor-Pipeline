from services.kafka.sub import Sub
from dal import Loader
from services.kafka.pub import Pub

if __name__=='__main__':
    sub1 = Sub('enriched', 'antisemitic')
    sub2 = Sub('enriched', 'not_antisemitic')
    sub1.connect()
    sub2.connect()
    loader = Loader()
    processing1 = loader.load_to_mongodb(sub1.sub(),'antisemitic')
    processing2 = loader.load_to_mongodb(sub2.sub(),'not_antisemitic')
    pub1 = Pub('','')
    pub2 = Pub('','')
    pub1.connect()
    pub2.connect()
    pub1.pub(processing1,'tweets_antisemitic')
    pub2.pub(processing2,'tweets_not_antisemitic')