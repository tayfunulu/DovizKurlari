FROM python:slim


ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

CMD python /app/flask_doviz_server.py
