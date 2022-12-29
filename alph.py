#!/usr/bin/env python3

import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("infile", type=str, help="path to file for modification")
parser.add_argument("-o", "--outfile", type=str, help="path to destination")
args = parser.parse_args()

try:
    img = cv2.imread(args.infile) #pyright:ignore

except FileNotFoundError:
    print("File not found")
    exit(1)

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("ting", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
