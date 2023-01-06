import json
import time
import random as r

from kafka import KafkaProducer

KAFKA_TOPIC = "input_data"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(1, ORDER_LIMIT):
  data = {
    "id": i,
    "rh": r.randint(1,10),
    "lh": r.randint(1,10),
    "op": "add",
  }

  producer.send(KAFKA_TOPIC, 
    json.dumps(data).encode("utf-8"))
  print(f"Done Sending..{i}")
  time.sleep(1)