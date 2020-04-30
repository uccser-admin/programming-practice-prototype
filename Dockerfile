# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM uccser/django:2.2.3

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ENV DJANGO_PRODUCTION=True

RUN apt-get update \
    && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    cron \
    --no-install-recommends --no-install-suggests \
    && apt-get -y --purge autoremove \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8080
RUN mkdir /codewof
WORKDIR /codewof

# Copy and install Python dependencies
COPY requirements /requirements
RUN /docker_venv/bin/pip3 install -r /requirements/production.txt

ADD ./codewof /codewof/

CMD /codewof/docker-production-entrypoint.sh
