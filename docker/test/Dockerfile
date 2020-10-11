FROM python:3.7
FROM jupyter/minimal-notebook
WORKDIR $HOME
RUN python -m pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN python -m pip  install -r requirements.txt  --ignore-installed


#

USER root
RUN apt-get update
RUN  apt-get -y install python-pydot
RUN  apt-get -y install python-pydot-ng
RUN  apt-get -y install graphviz
RUN rm -rf /var/lib/apt/lists/*

