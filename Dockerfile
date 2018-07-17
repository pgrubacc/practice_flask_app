FROM python:3.6-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev openssl-dev
COPY requirements.txt requirements.txt
#RUN python -m venv venv
#RUN venv/bin/pip install --upgrade pip
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install gunicorn pymysql
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql


COPY app app
COPY migrations migrations
COPY blog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP blog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
