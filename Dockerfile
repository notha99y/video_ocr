# docker file to run ocr on videos
FROM continuumio/miniconda3

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install tesseract-ocr libtesseract-dev
RUN conda install -c conda-forge opencv=4.1.0
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get -y install --reinstall libxcb-xinerama0
RUN apt-get -y install libqt5x11extras5
RUN pip install --upgrade pip
RUN pip install pillow pytesseract imageio