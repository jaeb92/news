import yaml
from kafka.admin import KafkaAdminClient, NewTopic

with open('kafka/config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
    
admin_client = KafkaAdminClient(
    bootstrap_servers=config['brokers'],
)

new_topic_name = 'test'
new_topic_part = 3
new_topic_repl = 3

topic_list = [
    NewTopic(name=new_topic_name, num_partitions=new_topic_part, replication_factor=new_topic_repl),
]

admin_client.create_topics(new_topics=topic_list, validate_only=False)