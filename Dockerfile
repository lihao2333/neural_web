FROM tensorflow/tensorflow:latest
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install Pillow
RUN pip3 install Django==2.0.2

