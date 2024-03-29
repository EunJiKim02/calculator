import json
import time
import random as r

from kafka import KafkaProducer


KAFKA_TOPIC = "input_data"
ORDER_LIMIT = 15



producer = KafkaProducer(bootstrap_servers='host.docker.internal:9092')
i = 0
while(True):
  lh, rh = map(int, input("input lh, rh >>> ").split())

  op = input("choose (add sub mul div) >> ")
  data = {
    "id": i,
    "rh": rh,
    "lh": lh,
    "op": op,
  }
  i = i + 1
  producer.send(KAFKA_TOPIC, 
    json.dumps(data).encode("utf-8"))
  if(lh == 0 and rh == 0):
    break
  print(f"Done Sending..{i}")
  time.sleep(1)