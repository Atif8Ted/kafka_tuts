import json
import time

from kafka import KafkaProducer
from get_tweet_data import get_twitter_data

kafka_topic = "twitter_tweet"
producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    for i in get_twitter_data():
        producer.send(kafka_topic, json.dumps({"id": i}).encode("utf-8"))
        producer.flush()
    time.sleep(60)

