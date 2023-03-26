import time

from kafka import KafkaProducer
import json
from data import get_registered_user

TOPIC_NAME_SINGLE_PARTITION = "registered_users"
TOPIC_NAME_TWO_PARTITION = "registered_user_2_partition"


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["192.168.0.106:9092"], value_serializer=json_serializer
)


def produce_messages(topic):
    user = get_registered_user()
    print(user)
    producer.send(topic=topic, value=user)


if __name__ == "__main__":
    while True:
        produce_messages(topic=TOPIC_NAME_SINGLE_PARTITION)
        produce_messages(topic=TOPIC_NAME_TWO_PARTITION)