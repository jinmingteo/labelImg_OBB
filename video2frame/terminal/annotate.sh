#!/bin/sh
xhost +local:docker && docker run --rm -e "DISPLAY=${DISPLAY}" -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" -v $offline_annotation_repo:/workspace/videos offline_annotator
