from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


admin_client = KafkaAdminClient(bootstrap_servers=["192.168.0.106:9092"])
topic_name = "registered_users"
num_partitions = 1
replication_factor = 1

new_topic = NewTopic(
    name=topic_name,
    num_partitions=num_partitions,
    replication_factor=replication_factor,
)
try:
    admin_client.create_topics([new_topic])
    print(f"{topic_name} created")
except TopicAlreadyExistsError:
    print(f"{topic_name} already exists")
