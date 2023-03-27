from kafka import KafkaConsumer
import json

TOPIC_NAME_SINGLE_PARTITION = "registered_users"
if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC_NAME_SINGLE_PARTITION,
        bootstrap_servers="192.168.0.106:9092",
        auto_offset_reset="earliest",
        group_id="con-grp-a",
    )
    print("starting the consumer")
    for message in consumer:
        # since while sending we were serializing it ,
        # so we need to deserialize it using json.loads and message.value
        print(json.loads(message.value))
