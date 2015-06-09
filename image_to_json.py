#!/usr/bin/env python
"""Converts image to json-like file.

Usage:
    image_to_json.py (-i FILE) [-o FILE] [-s K] [-f FILTER]

Options:
    -h --help                   Shows this screen.
    -i FILE --input=FILE        Input image file.
    -o FILE --output=FILE       Output json file. [default: image.json]
    -s K --size=K               Resize image in K. [default: False]
    -f FILTER --filter=FILTER   Resampling filter, NEAREST, BILINEAR, BICUBIC or LANCZOS. [default: NEAREST]
"""


import os
import sys
import getopt
from docopt import docopt

import json

from PIL import Image


def get_filter(resample):
    if resample.upper() == 'NEAREST':
        f = Image.NEAREST
    elif resample.upper() == 'BILINEAR':
        f = Image.BILINEAR
    elif resample.upper() == 'BICUBIC':
        f = Image.BICUBIC
    elif resample.upper() == 'LANCZOS':
        f = Image.LANCZOS
    else:
        f = Image.NEAREST
    return f

def get_pixels(fname, size=False, resample='NEAREST'):
    image = Image.open(fname)
    width, height = image.size

    if size.upper() != 'FALSE':
        width = int(width*float(size))
        height = int(height*float(size))
        image = image.resize((width, height), resample=get_filter(resample))

    pixels = list(image.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    if type(pixels[0][0]) is not int:
        pixels = [[p[0] for p in row] for row in pixels]

    return pixels

def write_json(fname, pixels):
    with open(fname, 'w') as f:
        return f.write(json.dumps(pixels, indent=4))

if __name__ == '__main__':
    args = docopt(__doc__)
    img = get_pixels(args['--input'],
                     size=args['--size'],
                     resample=args['--filter'])
    write_json(args['--output'], img)
