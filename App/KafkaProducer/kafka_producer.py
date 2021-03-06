from confluent_kafka import Producer
from AppConfiguration.config import KafkaConfig
import json
import time

class KafkaProducer():
    # Initialise properties
    kafka_config = KafkaConfig()
    bootstrap_servers_address = kafka_config.bootstrap_servers_address
    first_topic_name = kafka_config.first_topic_name
    linger_time_in_ms = 20
    batch_size_in_bytes = 32*1024 # 32KB

    # Create Kafka config dictionary
    kafkaProducerConfig = {
        'bootstrap.servers': bootstrap_servers_address[0],
        # Safe Producer config
        'enable.idempotence': "true", # Safe Producer sets Acks = all, retries.config = integer.max_value, and max_in_flight_requests = 5
        # High throughput Producer config
        'compression.type': 'snappy',
        'linger.ms': str(linger_time_in_ms),
        'message.max.bytes' : str(batch_size_in_bytes)
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