FROM python:3.9

WORKDIR /usr/src
COPY ["getdata.py", "."]

RUN pip3 install --upgrade pip && pip install psycopg2
RUN pip install kafka-python

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD ["getdata.py" ]