FROM python:3.9-slim-buster

WORKDIR app
ENV PYTHONPATH="${PYTHONPATH}:app"
COPY requierements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./ .

ENTRYPOINT ["python3", "src/cli.py"]
