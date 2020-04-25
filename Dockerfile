FROM python:3.7-slim

WORKDIR /usr/src/flaskr

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl g++ && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./flaskr ./flaskr

CMD [ "python", "-u", "-m", "flaskr" ]
