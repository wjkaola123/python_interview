from kafka import KafkaProducer
import json

# Define a dictionary representing a JSON object
data = {"id": 1, "name": "Alice", "age": 25}

# Convert the dictionary to JSON string format
json_string = json.dumps(data)

# Create producer instance with JSON serializer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Send the message to the topic 'test'
producer.send('my-topic', value=data)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()

# Close the producer connection
producer.close()