FROM python:3.6


COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./backend/dietacukrzyka /code/backend


COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]