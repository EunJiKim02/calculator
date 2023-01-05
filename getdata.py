import json

from kafka import KafkaConsumer

KAFKA_TOPIC = 'input_data'

consumer = KafkaConsumer(
  KAFKA_TOPIC,
  bootstrap_servers="localhost:9092"
)


print("start listening")

while True:
  for message in consumer:
    print("get data")
    consumed_message = json.loads(message.value.decode())
    
    ex_id = consumed_message["id"]
    ex_rh = consumed_message["rh"]
    ex_lh = consumed_message["lh"]
    ex_op = consumed_message["op"]
    
    if(ex_op == "add"):
      result = ex_rh + ex_lh
    elif(ex_op == "sub"):
      result = ex_rh - ex_lh
    elif(ex_op == "mul"):
      result = ex_rh * ex_lh
    else:
      result = ex_rh / ex_lh

    data = {
    "id": ex_id,
    "rh": ex_rh,
    "lh": ex_lh,
    "op": "add",
    "result": result
    }
    print(f"{ex_id} => {ex_rh} {ex_op} {ex_lh} = {result}")