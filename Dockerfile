FROM kaixhin/cuda-torch:8.0
RUN add-apt-repository ppa:mc3man/trusty-media
RUN apt-get update -y
RUN apt-get install libprotobuf-dev protobuf-compiler python3-pip  ffmpeg vim -y
RUN pip3 install Pillow
RUN pip3 install Django==2.0.2
RUN pip3 install pandas
RUN pip3 install --upgrade pip
RUN pip3 install opencv-python
RUN pip3 install --ignore-installed six
RUN pip3 install tensorflow==1.5.0
RUN luarocks install loadcaffe
