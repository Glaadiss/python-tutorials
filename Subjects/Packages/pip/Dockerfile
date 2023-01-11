FROM ubuntu:20.04
RUN apt-get update && apt-get install -y gnuplot python3.9
COPY requirements.txt .
RUN pip install -r requirements.txt