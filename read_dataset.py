import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd

mat = loadmat('..SBJ01\\trainData.mat')  # load mat-file
mdata = mat['measuredData']  # variable in mat file
