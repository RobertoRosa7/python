#
# Pets-API Dockerfile
#

# Pull base image
FROM python:3

# Get some custom packages
RUN apt-get update && apt-get install -y \
  build-essential \
  make \
  gcc \
  python3-dev \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 \
  echo "deb http://repo.mongodb.org/apt/debian "$(lsb_release -sc)"/mongodb-org/4.0 main" | tee /etc/apt/sources.list.d/mongodb.list \
  mongodb-org

# Make local directory
RUN mkdir /opt/pets-api

# Set 'pets-api' as working directory
WORKDIR /opt/pets-api

# copy all file
ADD . .

# PIP install
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# listen on port
EXPOSE 5000

# start
CMD ls