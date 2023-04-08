from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


admin_client = KafkaAdminClient(bootstrap_servers=["192.168.0.106:9092"])
topic_name = "registered_users_1_part"
num_partitions = 1
replication_factor = 1

new_topic_with_1_partition = NewTopic(
    name=topic_name,
    num_partitions=num_partitions,
    replication_factor=replication_factor,
)
new_topic_with_2_partition = NewTopic(
    name="registered_user_2_partition", num_partitions=2, replication_factor=1
)
message_to_fix_partition = NewTopic(
    name="message_to_fix_partition", num_partitions=2, replication_factor=1
)
topics = [
    # new_topic_with_1_partition,
    new_topic_with_2_partition,
    # message_to_fix_partition,
]
for topic in topics:
    try:
        admin_client.create_topics([topic])
        # admin_client.delete_topics([topic])
        print(f"{topic} created")
    except TopicAlreadyExistsError as e:
        print(e.message)






