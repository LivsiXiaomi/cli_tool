FROM python:3.9-slim-buster

WORKDIR app

COPY requierements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "src/cli.py", "--input_file=tests/test_data/valid_data.txt"]
