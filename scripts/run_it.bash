#!/bin/bash

# Update this to point to the image you
# want to use

SOURCE_PATH="/Users/alan/Graphics/misc/magritte-son-of-man-1964.jpg"

# The process

printf "%s" $SOURCE_PATH > source-path.txt
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pillow
python convert.py
deactivate
#rm -rf vev




