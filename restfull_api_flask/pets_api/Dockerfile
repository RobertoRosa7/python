#
# Pets-API Dockerfile
#

# Pull base image
FROM python:3.4.5-slim

# Get some custom packages
RUN apt-get update && apt-get install -y \
  build-essential \
  make \
  gcc \
  python3-dev \
  mongodb

# Make local directory
RUN mkdir /opt/pets-api

# Set 'pets-api' as working directory
WORKDIR /opt/pets-api

# coe all file
ADD . .

# PIP install
RUN pip install -r requirements.txt

# listen on port
EXPOSE 5000

# start
CMD python manage.py runserver