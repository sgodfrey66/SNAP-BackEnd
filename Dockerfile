FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install --system
ADD src/ /code/
