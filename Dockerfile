FROM python:3.10-slim-buster

ENV PYTHONBUFFERED = 1
WORKDIR /job_search
COPY job_search/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY job_search .
EXPOSE 8000
CMD ["python","manage.py","runserver"]
