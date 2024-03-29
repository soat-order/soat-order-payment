FROM python:3.9.18

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# install dependencies
COPY ./requirements.txt ./
COPY ./app/.env-settings-prd ./.env-settings
RUN apt upgrade
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 uninstall PyJWT -y
RUN pip3 install PyJWT==2.8.0

# copy project
COPY ./app ./