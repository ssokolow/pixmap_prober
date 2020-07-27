#!/usr/bin/env python3

import sys
from PIL import Image

with open(sys.argv[1], 'rb') as fobj:
    data = fobj.read()

OFFSET = 5
WIDTH = 8
HEIGHT = len(data) // WIDTH

data = data[OFFSET:]
img = Image.frombytes(
    "1", (WIDTH, HEIGHT), data[:WIDTH * HEIGHT], "raw", "1", 0, 1)
img.save(sys.argv[1] + '.png')
