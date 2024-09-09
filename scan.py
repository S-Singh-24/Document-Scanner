import pyimagesearch
from skimage.filters import threshold_local
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("'i", "--image", required = True,
                help = "Path to the image to be scanned")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

