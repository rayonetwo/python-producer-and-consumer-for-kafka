# Python Producer and Consumer Applications for Apache Kafka

## Description
The producer application sends messages to a Kafka topic(messages), which are then read by a Kafka consumer application. The consumer application then stores the consumed data to a cloud PostgreSQL database.

## Steps for Setup and Usage
* Install Docker (and docker-compose)
* Install Python
* Run `pip install kafka-python` to install `kafka-python`
* Run `pip install psycopg2` to install `psycopg2`
* Run `docker-compose -f docker-compose.yml up -d` to pull the images and create containers
* Run `docker exec -it kafka /bin/sh` to start a Kafka shell
* Navigate to `/opt/kafka_<version>/bin` where all Kafka scripts are located
* Run `kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic messages` to create `messages` topic
* Run `python consumer.py` to start the consumer which connects to a cloud PostgreSQL database. It reads latest messages from the Kafka topic `messages` and stores them to the database
* Run `python producer.py` to start the producer which sends messages to the topic `messages`
