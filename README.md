# Kafka Basics
This is a small kafka based project created for learning purpose. It creates a small producer and consumer and their integration.
Its written in python and quite easy to understand. The programs scrapes some information and puts those info inside a topic to behave like a producer
and the consumer reads that from the topic.


## Kafka
Kafka is a distributed and highly fault-tolerant messaging platform. The internals are complex where I/O(networking) plays 
an important role. In simple terms it can handle multiple producers and multiple consumers together writing and reading to same topic with high volume.

Topic(or so called Q) is like a folder where the messages(logs) are written. Some highlights about the keywords</p>
<li><b>Distributed</b>: It runs on multiple machines.
<li><b>Partitions</b>: It splits the topic into multiple partitions so that it can handle multiple writes by different producers
<li><b>Replication</b>: It replicates the same data into multiple times so it can handle failover.
<li><b>Offset</b>: An incremental sequence no that lets consumer know from where to read next so that only single copy can be read by multiple consumers.

## Pre-requisite
Java has to be installed on the machine. Please refer for installation https://www.java.com/en/download/help/download_options.html

## To Run
Kafka can be run on a single machine or multiple machine. This example uses a single machine/worker installation on mac.

## To install
Install Kafka from https://kafka.apache.org/downloads
We need to run 2 things before we create a topic.
1. A zookeeper service that helps in metadata management.
2. Kafka server, the master mind.

Then we can create a topic which can take data from producer and consumer.
```commandline
# install the dependencies
pipenv install

cd kafka_2.13-3.3.1(this is my version)

# start the zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# start the kafka server
bin/kafka-server-start.sh config/server.properties

# create a topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic raw_recipes

#To run
python src/main.py
```




