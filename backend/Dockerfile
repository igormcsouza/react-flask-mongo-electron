FROM python:3.8-alpine3.11

RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       python \
                       pkgconfig \
                       git \
                       gcc \
                       openldap \
                       libcurl \
                       python2-dev \
                       gpgme-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY *.lock *.toml /app/
RUN poetry install

COPY . /app

CMD gunicorn --bind 0.0.0.0:5000 backend.wsgi:app