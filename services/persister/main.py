from services.kafka.sub import Sub
from dal import Loader
from services.kafka.pub import Pub

if __name__=='__main__':
    sub1 = Sub('enriched', 'antisemitic')
    sub2 = Sub('enriched', 'not_antisemitic')
    sub1.connect()
    sub2.connect()
    processing1 = Loader.load_to_mongodb(sub1.sub())
    processing2 = Loader.load_to_mongodb(sub2.sub())
    pub1 = Pub()
    pub2 = Pub()
    pub1.connect()
    pub2.connect()
    pub1.pub(processing1)
    pub2.pub(processing2)