#!/bin/sh
xhost +local:docker && docker run --rm -e "DISPLAY=${DISPLAY}" -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" --user "$(id -u):$(id -g)" -v $offline_annotation_repo:/workspace/videos -v $classes:/workspace/data/predefined_classes.txt offline_annotator
