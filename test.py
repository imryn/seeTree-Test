import numpy as np
import matplotlib.pyplot as plt
import cv2
import csv


def creatingHistogram():
    # read image
    im = cv2.imread('Grayscale-Lena-Image.png')
    # calculate mean value from RGB channels and flatten to 1D array
    vals = im.mean(axis=2).flatten()
    # calculate histogram
    counts, bins = np.histogram(vals, range(257))
    #writing into CSV file
    writingIntoCSV(vals)
    #sorting the vals array
    sortingTheVals(vals)
    # plot histogram centered on values 0..255
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()

def writingIntoCSV(vals):
    my_file = open('tonals.csv', 'w')
    csv_writer = csv.writer(my_file, delimiter=',')
    csv_writer.writerows(map(lambda x: [x], vals))
    my_file.close()

def sortingTheVals(vals):
     vals[::-1].sort()
     print(vals)
    
creatingHistogram()