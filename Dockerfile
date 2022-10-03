FROM ubuntu:22.04

RUN apt-get update
RUN apt-get -y install cron


COPY requirements.txt .
COPY backend/ backend/
COPY charts/*.py charts/
COPY data/*.parquet data/
COPY ./*.py .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt


ENV SPEEDTEST_PARQUET=/data/
ENV SPEEDTEST_LOG=/log/



EXPOSE 5000
CMD flask  --app index run --host 0.0.0.0 --port 5000