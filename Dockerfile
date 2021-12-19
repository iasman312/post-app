FROM python:3.8

ENV PYTHONBUFFERED 1

WORKDIR /post-app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .


# run gunicorn
CMD gunicorn main.wsgi:application --bind 0.0.0.0:$PORT