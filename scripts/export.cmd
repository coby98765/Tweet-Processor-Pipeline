#build & push Docker Images

#data_retrieval
docker build -t coby98765/tpp-data_retrieval:v1 ./services/data_retrieval
docker push coby98765/tpp-data_retrieval:v1

#enricher
docker build -t coby98765/tpp-enricher:v1 ./services/enricher
docker push coby98765/tpp-enricher:v1

#persister
docker build -t coby98765/tpp-persister:v1 ./services/persister
docker push coby98765/tpp-persister:v1

#preprocessor
docker build -t coby98765/tpp-preprocessor:v1 ./services/preprocessor
docker push coby98765/tpp-preprocessor:v1

#retriever
docker build -t coby98765/tpp-retriever:v1 -f services/retriever/Dockerfile  .
docker push coby98765/tpp-retriever:v1


