import json

from kafka import KafkaConsumer
import psycopg2

KAFKA_TOPIC = 'input_data'

consumer = KafkaConsumer(
  KAFKA_TOPIC,
  bootstrap_servers="127.0.0.1:9092"
)

hostname = 'localhost'
database = 'Calculator'
username = 'admin'
pwd = 'mobuk'
port_id = 5432


try:
  conn = psycopg2.connect(
        host=hostname,
        password=pwd,
        port=port_id,
        user=username,
        dbname=database 
  )
  
  cur = conn.cursor()

  create_script = '''CREATE TABLE IF NOT EXISTS expression(
  id INT NOT NULL,
  lh INT NOT NULL,
  rh INT NOT NULL,
  op TEXT NOT NULL,
  result INT NOT NULL,
  create_at TIMESTAMPTZ DEFAULT now()
  );'''

  cur.execute(create_script)
  conn.commit()


  print("start listening")

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
      result = ex_lh - ex_rh
    elif(ex_op == "mul"):
      result = ex_rh * ex_lh
    else:
      result = ex_lh / ex_rh

    data = {
    "id": ex_id,
    "rh": ex_rh,
    "lh": ex_lh,
    "op": ex_op,
    "result": result
    }
    if(ex_lh == 0 and ex_rh == 0):
      break

    insert_script = ''' INSERT INTO expression (id, lh, rh, result, op) 
    VALUES (%d, %d, %d, %d, '%s')'''%(ex_id, ex_lh, ex_rh, result, ex_op)

    cur.execute(insert_script)
    conn.commit()

    print(f"{ex_id} >> {ex_lh} {ex_op} {ex_rh} = {result}")



  cur.close()
  conn.close()
except Exception as e:
  print(e)
