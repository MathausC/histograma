from __future__ import print_function
from __future__ import division
from pickletools import uint8
import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
parser.add_argument('--input', help='Path to input image.', default='images/mergulhador.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
xlabel = "Escala de Cinza"
ylabel = "Intensidade da Cor"

bgr_planes = cv.split(src)[1]

bgr_planes2 = bgr_planes.copy()

values, count = np.unique(bgr_planes, return_counts=True)

percent_count = count/sum(count)

percent_cumsum = np.cumsum(percent_count)

not_rounded_values = percent_cumsum * max(values)

not_int_values = np.round(not_rounded_values)
new_values = not_int_values.astype(int)

for i in range(len(bgr_planes)):
    for j in range(len(bgr_planes[i])):
        index = np.where(values == bgr_planes[i][j])
        bgr_planes2[i][j] = new_values[index]

values2, count2 = np.unique(bgr_planes2, return_counts=True)

plt.bar(count, values)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()
plt.bar(count2, values2)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()