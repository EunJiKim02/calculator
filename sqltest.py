import psycopg2

hostname = 'localhost'
database = 'Calculator'
username = 'admin'
pwd = 'mobuk'
port_id = 5432

print("hihi")


try:
  #print("hi")
  conn = psycopg2.connect(
        host=hostname,
        password=pwd,
        port=port_id,
        user=username,
        dbname=database 
  )
  
  #conn = psycopg2.connect(pg_uri)

  cur = conn.cursor()

  print("hi")

  create_script = '''CREATE TABLE IF NOT EXISTS expression(
    id INT NOT NULL,
    lh INT NOT NULL,
    rh INT NOT NULL,
    op TEXT NOT NULL,
    create_at TIMESTAMPTZ DEFAULT now()
    );'''

  cur.execute(create_script)
  conn.commit()

  cur.close()
  conn.close()
except Exception as e:
  print(e)

  