import time

from kafka import KafkaProducer
import json
from data import get_registered_user

TOPIC_NAME_SINGLE_PARTITION = "test_partition"


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partition(key, all, available):
    # return partition 0
    return 0


producer = KafkaProducer(
    bootstrap_servers=["192.168.0.106:9092"], value_serializer=json_serializer
)
producer_fix_partition = KafkaProducer(
    bootstrap_servers=["192.168.0.106:9092"],
    value_serializer=json_serializer,
    partitioner=get_partition,
)


def produce_messages(topic, producer_name):
    user = get_registered_user()
    print(json.dumps(user))
    producer_name.send(topic=topic, value=user)


if __name__ == "__main__":
    while True:
        produce_messages(topic=TOPIC_NAME_SINGLE_PARTITION, producer_name=producer)
        time.sleep(4)
