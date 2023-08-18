import json
import yaml
# python kafka client
from kafka import KafkaProducer
from kafka.errors import KafkaError

with open('kafka/config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)            
print(config)
exit()
producer = KafkaProducer(
            # bootstrap_servers=['kafka-1:9092', 'kafka-2:9092', 'kafka-3:9092'],
            bootstrap_servers=config['brokers']
            )      
# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError as e:
    # Decide what to do if produce request failed...
    print(e)
    pass