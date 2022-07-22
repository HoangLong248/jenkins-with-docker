FROM python:3.9-alpine
MAINTAINER Long Tran

RUN python -m pip install flask

COPY rest_with_docker.py .

ENTRYPOINT ["python", "rest_with_docker.py"]
