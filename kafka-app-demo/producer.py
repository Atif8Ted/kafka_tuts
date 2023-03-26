import time

from kafka import KafkaProducer
import json
from data import get_registered_user

TOPIC_NAME = "registered_users"


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["192.168.0.106:9092"], value_serializer=json_serializer
)


def produce_messages():
    user = get_registered_user()
    print(user)
    producer.send(topic=TOPIC_NAME, value=user)


if __name__ == "__main__":
    while True:
        produce_messages()
        time.sleep(4)
