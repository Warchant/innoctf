FROM ubuntu:trusty
MAINTAINER Alexey Rodionov <rodionov12@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -yqq update && \
    apt-get -yqq install python3 python3-pip && \
    apt-get clean

COPY static/ /root
# Define working directory.
WORKDIR /root/static

EXPOSE 31265

# start app
CMD [ "python3", "./server.py" ]
