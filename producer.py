import json
import time
import random
from message_generator import create_message
from kafka import KafkaProducer

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        message = create_message()

        # Send message to messages topic
        producer.send('messages', message)

        # Sleep for random number of seconds
        time.sleep(random.randint(1, 10))
