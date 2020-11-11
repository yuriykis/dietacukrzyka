FROM python:3.6


COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./dietacukrzyka /code/dietacukrzyka
COPY ./manage.py /code/manage.py


COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]