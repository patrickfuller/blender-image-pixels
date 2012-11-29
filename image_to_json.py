#!/usr/bin/env python
"""
Opens image and converts to csv data using the PIL library
"""

import Image
from sys import argv, exit
import json

if len(argv) != 2:
    print "USAGE: python image_to_csv.py *image_name*"
    exit()

image = Image.open(argv[1])
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i*width:(i+1)*width] for i in range(height)]

# Use first value if multi channel
if type(pixels[0][0]) is not int:
    pixels = [[p[0] for p in row] for row in pixels]

print json.dumps(pixels, indent=4)
