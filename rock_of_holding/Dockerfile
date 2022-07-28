FROM python:3.9-slim

# captures all python outputs
ENV PYTHONBUFFERED=1

# TODO: figure out what I need here
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    nginx

COPY rock_of_holding/requirements/prod ./requirements/prod
COPY rock_of_holding/requirements/dev ./requirements/dev
RUN pip install -r ./requirements/prod
RUN pip install -r ./requirements/dev

ADD . /app
WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "rock_of_holding.wsgi"]
