# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir "app"
WORKDIR /app

COPY . /app/
#COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["bash", "/app/entrypoint.sh"]