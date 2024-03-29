FROM python:3.9.16

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt ./
RUN echo ${PWD} && ls -lR
COPY /home/runner/work/soat-order-payment/soat-order-payment/app/.env-prd /home/runner/work/soat-order-payment/soat-order-payment/app/.env-settings
RUN apt upgrade
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY ./app ./
