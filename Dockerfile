FROM python:3.10

LABEL maintainer="Enes Gulakhmet <wwho.mann.3@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y netcat
RUN pip install --upgrade pip && pip install poetry

RUN mkdir /app
COPY /app /app
COPY pyproject.toml /app
WORKDIR /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000
