FROM ubuntu
RUN apt-get update
RUN apt-get install --yes python3
RUN apt-get install --yes build-essential
RUN apt-get install --yes python3-pip
RUN apt-get install --yes python3-virtualenv

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#RUN pip3 install flask
#RUN rm requirements.txt