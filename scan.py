import pyimagesearch
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("'i", "--image", required = True,
                help = "Path to the image to be scanned")
args = vars(ap.parse_args())

