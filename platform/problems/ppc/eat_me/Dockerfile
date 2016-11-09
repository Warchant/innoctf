FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -yqq update && \
    apt-get -yqq install python3 python3-pip && \
    apt-get clean

COPY static/ /root

EXPOSE 47139

WORKDIR /root
CMD [ "python3", "server.py" ]
