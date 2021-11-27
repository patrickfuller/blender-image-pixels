#!/usr/bin/env python
"""usage: image_to_json.py [-h] -i INPUT [-o OUTPUT] [-s SIZE] [-f FILTER]

Converts image to json file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input image file.
  -o OUTPUT, --output OUTPUT
                        Output json file.
  -s SIZE, --size SIZE  Reduce image by a proportional factor.
  -f FILTER, --filter FILTER
                        Resampling filter. Can be 'nearest', 'bilinear',
                        'bicubic', or 'lanczos'.

"""

import argparse
import json

from PIL import Image


def get_pixels(fname, size=1, resample='nearest'):
    image = Image.open(fname)
    width, height = image.size

    if size <= 0:
        raise ValueError("Size must be a positive value.")
    elif size > 1:
        raise ValueError("Size is specified as a proportion, not a percent.")
    elif size != 1:
        width = int(width * float(size))
        height = int(height * float(size))
        image = image.resize((width, height),
                             resample=getattr(Image, resample.upper()))

    pixels = list(image.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    if type(pixels[0][0]) is not int:
        pixels = [[p[0] for p in row] for row in pixels]

    return pixels


def write_json(fname, pixels):
    with open(fname, 'w') as f:
        return f.write(json.dumps(pixels, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Converts image to json file.")
    parser.add_argument('-i', '--input',
                        type=str,
                        required=True,
                        help="Input image file.")
    parser.add_argument('-o', '--output',
                        type=str,
                        default='pixels.json',
                        help="Output json file.")
    parser.add_argument('-s', '--size',
                        type=float,
                        default=1,
                        help="Reduce image by a proportional factor.")
    parser.add_argument('-f', '--filter',
                        type=str,
                        default='nearest',
                        help=("Resampling filter. Can be 'nearest', "
                              "'bilinear', 'bicubic', or 'lanczos'."))
    args = parser.parse_args()

    img = get_pixels(args.input, size=args.size, resample=args.filter)
    write_json(args.output, img)
