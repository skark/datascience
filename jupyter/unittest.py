import sys
import matplotlib as matplot
import numpy as np
import sklearn
import cv2
import tensorflow as tf
import keras
import torch
import scipy
import pandas as pd

print("Python Version: " + sys.version)
print("Matplotlib version: " + matplot.__version__)
print("Matplotlib numpy version: " + matplot.__version__numpy__)
print("Numpy version: " + np.__version__)
print("Scikit version: " + sklearn.__version__)
print("OpenCV version: " + cv2.__version__)
print("Tensorflow version: " + tf.__version__)
print("Keras version: " + keras.__version__)
print("Pytorch version:" + torch.__version__)
print("Scipy version:" + scipy.version.full_version)
print("Pandas version:" + pd.__version__)
print(pd.show_versions(as_json=False))
