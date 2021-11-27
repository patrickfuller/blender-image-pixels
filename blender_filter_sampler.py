#!/usr/bin/env python
"""
Generates various filter kernels for use in Blender drawing
"""

from math import exp, sin, cos, pi, sqrt, log
import json


def scale(kernel):
    """ Scales a 2D array to [0, 255] """
    minimum = min(min(k) for k in kernel)
    maximum = max(max(k) for k in kernel)
    return [[int(255 * (k - minimum) / (maximum - minimum)) for k in row]
            for row in kernel]

# Gradient kernels
basic_x = scale([[0, 0, 0], [0, -1, 1], [0, 0, 0]])
basic_y = scale([[0, 0, 0], [0, -1, 0], [0, 1, 0]])
sobel_x = scale([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = scale([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
scharr_x = scale([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
scharr_y = scale([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])


def generate_gaussian(sigma=3.0, size=21):
    """Generates a 2D Gaussian function scaled to [0, 255]"""
    return [[gauss(x - (size - 1) / 2, y - (size - 1) / 2, sigma)
             for y in range(size)] for x in range(size)]


def generate_fourier(wavelength=8, direction=0, size=21):
    """Generates a 2D Fourier function scaled to [0, 255]"""
    return [[fourier(x - (size - 1) / 2, y - (size - 1) / 2, wavelength,
             direction) for y in range(size)] for x in range(size)]


def generate_gabor(wavelength=8, direction=0, sigma=None, size=21):
    """Generates a 2D Gabor kernel scaled to [0, 255]"""
    gauss = lambda x, y: 1 / (2 * pi * sigma) * exp(-(x ** 2 + y ** 2)
                                                    / (2 * sigma ** 2))
    fourier = lambda x, y: cos(
        2 * pi / wavelength * (x * cos(direction) + y * sin(direction)))
    gabor = lambda x, y: gauss(x, y) * fourier(x, y)

    # Half-response spatial-frequency bandwidth. Keeps oscillation dampening
    # constant for all input wavelengths. Use if sigma is not specified.
    if sigma is None:
        octave = 1
        sigma = wavelength * 1 / pi * sqrt(log(2) / 2) * (
            2 ** octave + 1) / (2 ** octave - 1)

    kernel = [[gabor(x - (size - 1) / 2, y - (size - 1) / 2)
               for y in range(size)] for x in range(size)]
    # Manually calculate min and max, as Gabor can be weird
    return scale(kernel)


def gauss(x, y, sigma):
    """Evaluates the Gaussian function"""
    return 1 / (2 * pi * sigma) * exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))


def fourier(x, y, lambda_, theta):
    """Evaluates the Gaussian function"""
    return cos(2 * pi / lambda_ * (x * cos(theta) + y * sin(theta)))


def gabor(x, y, lambda_, theta, sigma=None):
    """Evaluates the Gabor function, optionally deriving sigma"""
    # Half-response spatial-frequency bandwidth. Keeps oscillation dampening
    # constant for all input wavelengths. Use if sigma is not specified.
    # Assumes one octave. Can change by replacing 3 with (2^n+1)/(2^n-1)
    if sigma is None:
        sigma = 3 * lambda_ * 1 / pi * sqrt(log(2) / 2)
    return fourier(x, y, lambda_, theta) * gauss(x, y, sigma)


def draw_image(pixels, filename):
    """Converts a generated kernel to a 2D image"""
    from PIL import Image
    img = Image.new("L", size=(len(pixels), len(pixels[0])))
    for x, row in enumerate(pixels):
        for y, pixel in enumerate(row):
            img.putpixel((x, y), pixel)
    img.save(filename)


# Get pixels
pixels = scale(generate_gaussian(sigma=3.0, size=21))
draw_image(pixels, "gaussian2D.png")
pixels = scale(generate_fourier(direction=pi/4, size=49))
draw_image(pixels, "fourier2D.png")
pixels = scale(generate_gabor(direction=pi / 4))
draw_image(pixels, "gabor2D.png")
