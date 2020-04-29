from confluent_kafka import Producer
from AppConfiguration.config import KafkaConfig
import json
import time

class KafkaProducer():
    # Initialise properties
    kafka_config = KafkaConfig()
    bootstrap_servers_address = kafka_config.bootstrap_servers_address
    first_topic_name = kafka_config.first_topic_name

    # Create Kafka config dictionary
    kafkaProducerConfig = {
        'bootstrap.servers': bootstrap_servers_address[0]
    }

    def __init__(self):
        self.producer = Producer(self.kafkaProducerConfig)

    def _event_created(self, err, msg):
        if err is not None:
            retval = {"message": "Failed to deliver message: {0}: {1}".format(msg.value(), err.str())}, 500
        else:
            retval = {"message": "Message Sent: {0}".format(msg.value())}, 201

    def send_message(self, message):
        self.producer.produce(self.first_topic_name, value=message, on_delivery=self._event_created)
        self.producer.flush()