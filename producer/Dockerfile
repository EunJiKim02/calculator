FROM ubuntu:18.04

RUN apt update && apt-get install -y python3
RUN apt install python3-pip -y

WORKDIR /usr/src
COPY ["randomdata.py", "."]
COPY ["insertdata.py", "."]

RUN pip3 install --upgrade pip && pip3 install psycopg2
RUN pip3 install kafka-python

# docker exec -it calculator-producer-1 bash
# python3 insertdata.py
