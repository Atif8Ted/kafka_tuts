import sqlite3

from kafka import KafkaConsumer
import json

kafka_topic = "twitter_tweet"
conn = sqlite3.connect("twitter.sqlite")
c = conn.cursor()
c.execute("""CREATE TABLE my_table (id INTEGER PRIMARY KEY, data TEXT)""")
# connect to already existing sqlite db called twitter.sqlite


consumer = KafkaConsumer(kafka_topic, bootstrap_servers="localhost:9092")
for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    print(data)
    c.execute("INSERT INTO my_table (data) VALUES (?)", (json.dumps(data),))
    conn.commit()
