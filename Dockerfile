# docker build . -t offline_annotator
# xhost +local:docker && docker run --rm -e "DISPLAY=${DISPLAY}" -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" offline_annotator

FROM python:3.6-slim

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    pyqt5-dev-tools \
    libxml2-dev libxslt1-dev \
    python3-tk \
    make

WORKDIR /workspace

COPY . /workspace/
RUN pip install -r requirements/requirements-linux-python3.txt
RUN make qt5py3

CMD [ "python", "labelImg.py" ]