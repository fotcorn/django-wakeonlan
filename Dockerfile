
FROM python:3.7-slim AS builder


RUN set -ex \
    && apt-get update \
    && apt-get install build-essential --no-install-recommends -y \
    && pip install pipenv

ADD ./Pipfile /Pipfile
ADD ./Pipfile.lock /Pipfile.lock

RUN set -ex \
    && pipenv install --system --deploy \
    && pip install uwsgi==2.0.17

# create new container without build dependencies
FROM python:3.7-slim

# copy site-packages with compiled binaries from builder container
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# copy code into container
RUN mkdir /code
ADD ./manage.py /code/manage.py
ADD ./wol/ /code/wol

ENV DEBUG False
ENV UWSGI_WSGI_FILE=/code/wol/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

WORKDIR /code
RUN SECRET_KEY=none python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["/usr/local/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
