import json
import time
import random as r

from kafka import KafkaProducer

KAFKA_TOPIC = "input_data"
ORDER_LIMIT = 15

n = int(input("time setting >> "))

producer = KafkaProducer(bootstrap_servers='host.docker.internal:9092')
i = 0
while(True):
  lh = r.randint(1, 100)
  rh = r.randint(1, 100)

  k = r.randint(1, 4)
  if(k == 1):
    op = 'add'
  elif (k == 2):
    op = 'sub'
  elif (k == 3):
    op = 'mul'
  elif (k == 4):
    op = 'div'

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

  time.sleep(n)