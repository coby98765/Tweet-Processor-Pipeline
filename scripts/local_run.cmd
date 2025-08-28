#pull MongoDB Image
docker pull mongodb/mongodb-community-server:latest

#run MongoDB container
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest

#run Kafka container
docker run -d --name=kafka -p 9092:9092 apache/kafka

# get kafka cluster id
docker exec -ti kafka /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server :9092

#create network
docker network create tpp-network

#connect container to network
docker network connect tpp-network mongodb
docker network connect tpp-network broker
docker network connect tpp-network <add-container-name-if-needed>

#Run Docker Container data_retrieval
docker run --name data_retrieval_v1 -d -p 8000:8000 `
 --network tpp-network `
  -e DB_NAME=Tweets `
  -e DB_HOST=mongodb `
  -e API_PORT=8000 `
  coby98765/tpp-data_retrieval:v1

#Run Docker Container retriever
docker run --name retrieval_v1 -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e DB_HOST=cluster0.6ycjkak.mongodb.net `
  -e DB_NAME=IranMalDB `
  -e DB_COLL=tweets `
  -e DB_USER=IRGC_NEW `
  -e DB_PASS=iran135 `
  coby98765/tpp-retriever:v1

#Run Docker Container preprocessor
docker run --name preprocessor_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=antisemitic `
  coby98765/tpp-preprocessor:v1

docker run --name preprocessor_non_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=non_antisemitic `
  coby98765/tpp-preprocessor:v1

#Run Docker Container enricher
docker run --name enricher_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=antisemitic `
    coby98765/tpp-enricher:v1

docker run --name enricher_non_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=non_antisemitic `
  coby98765/tpp-enricher:v1

#Run Docker Container persister
docker run --name persister_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=antisemitic `
  -e DB_NAME=Tweets `
  -e DB_HOST=mongodb `
  coby98765/tpp-persister:v1

docker run --name persister_non_anti -d `
 --network tpp-network `
  -e KAFKA_HOST=broker:9092 `
  -e TOPIC=non_antisemitic `
  -e DB_NAME=Tweets `
  -e DB_HOST=mongodb `
  coby98765/tpp-persister:v1