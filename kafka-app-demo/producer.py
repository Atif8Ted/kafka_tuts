import time

from kafka import KafkaProducer
import json
from data import get_registered_user

TOPIC_NAME_SINGLE_PARTITION = "registered_users"
TOPIC_NAME_TWO_PARTITION = "registered_user_2_partition"


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
        produce_messages(topic=TOPIC_NAME_TWO_PARTITION, producer_name=producer)
        # Above the producer was sending to different partition of a topic randomly.
        # Now we want to send message to fixed partition of a topic
        # producer can select the partition of their choice in a topic where it wants to publish the message
        # lets define a different producer as producer_fix_partition
        produce_messages(
            topic="message_to_fix_partition", producer_name=producer_fix_partition
        )  # this will write data to partition 0 only
        time.sleep(4)
