FROM python:3.12-slim-bookworm

ENV APP_HOME=/app
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

LABEL maintainer='kpranav122005@gmail.com'
LABEL description='Development image for Real Estate Project'

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \ 
    && apt-get install -y gettext \
    && apt-get install -y netcat-openbsd gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY ./docker/local/django/celery/worker/start /start-celery-worker
RUN sed -i 's/\r$//g' /start-celery-worker
RUN chmod +x /start-celery-worker

COPY ./docker/local/django/celery/flower/start /start-celery-flower
RUN sed -i 's/\r$//g' /start-celery-flower
RUN chmod +x /start-celery-flower


ENTRYPOINT [ "/entrypoint" ]



