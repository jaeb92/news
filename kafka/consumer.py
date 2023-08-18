import json
import yaml
from kafka import KafkaConsumer

with open('kafka/config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
consumer = KafkaConsumer(
    'test333',
    bootstrap_servers=config['brokers'],
    value_deserializer=lambda x: json.loads(x)
)

for msg in consumer:
    print(msg)