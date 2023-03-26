from kafka import KafkaProducer
import json
from data import get_registered_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["192.168.0.106:9092"], value_serializer=json_serializer
)

# create a topic if it does not exist called "registered_users" with 1 partition and 1 replica
# producer.send("registered_users", value=get_registered_user())



# if __name__ == "__main__":
#     while True:
#         user = get_registered_user()
#         producer.
