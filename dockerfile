FROM python:latest
WORKDIR /SHET
COPY requirements.txt /SHET
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /SHET