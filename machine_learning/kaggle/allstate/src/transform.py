"""
Transform data before modeling

author: chris
"""

from wrappers import debug
import pandas as pd
import numpy as np
import os

@debug
def load(filename):
	"""Load Data from .csv"""
	#Load data into panda and numpy array
	data = pd.io.parsers.read_csv(filename, header = 0).values
	return data



if __name__ == "__main__":
	data = load(os.path.join("..","data","train.csv"))