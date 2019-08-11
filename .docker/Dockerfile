FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    software-properties-common \
    python3-tk \
    python3-setuptools

RUN /usr/bin/pip3 install --upgrade pip &&\
    pip3 --no-cache-dir install \
    numpy \
    scipy \
    Pillow \
    matplotlib \
    plotly==4.0.0 \
    notebook>=5.3 \
    ipywidgets>=7.2

RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
    apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    python3-gdal