#!/usr/bin/env python
"""Converts image to json-like file.
"""


import os
import sys
import getopt

import Image
import json


params = {'sname': os.path.basename(sys.argv[0]),
          'h':('-h', '--help'),
          'i':', '.join(('-i IMAGE', '--input=IMAGE')),
          'idesc': 'Input image file, parsed using PIL library',
          'o':', '.join(('-o IMAGE', '--output=IMAGE')),
          'odesc': 'Output file, *.json',
          'fill':' ',
          'align':'<',
          'newline':'\n',
          'width':30,
          'start':4*' ',
          }

def help_msg():
    s = ('{newline}Usage: {sname} [options]{newline}'
         '{newline}Options:'
         '{newline}{start}{i:{fill}{align}{width}s}{idesc}'
         '{newline}{start}{o:{fill}{align}{width}s}{odesc}').format(**params)
    return s


def get_pixels(fname):
    image = Image.open(fname)
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    if type(pixels[0][0]) is not int:
        pixels = [[p[0] for p in row] for row in pixels]
    return pixels

def write_json(fname, pixels):
    with open(fname, 'w') as f:
        return f.write(json.dumps(pixels, indent=4))

if __name__ == '__main__':
    ifile = ''
    ofile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:',
                                   ['help', 'input=', 'output='])

    except getopt.GetoptError as err:
        print str(err)
        print help_msg()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print help_msg()
            sys.exit(0)

        elif opt in ('-i', '--input'):
            ifile = arg

        elif opt in ('-o', '--output'):
            ofile = arg

    write_json(ofile, get_pixels(ifile))
