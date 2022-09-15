from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

bgr_planes = cv.split(src)

values, count = np.unique(bgr_planes, return_counts=True)

print(values)


for i in range(len(bgr_planes)):
    for j in range(len(bgr_planes[i])):
        pass