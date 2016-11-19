FROM python:3
COPY static/ /root
RUN apt-get -y update && apt-get -yqq install locales; \
	locale-gen ru_RU.UTF-8
EXPOSE 47139

WORKDIR /root
CMD [ "python3", "server.py" ]
