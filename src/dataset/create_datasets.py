import pandas as pd

class Dataset(object):
	''' Job: Reads raw data, delegates to preprocess and EDA functions.'''
	def __init__(self, data_path):
		self.data_path = data_path

	def load_data(self):
		''' Loads data from data path and returns the dimensions of that dataset.
		 It verifies if the data path exists or not. If it does, it returns the
		 dimensions of the data at that location. It also loads the data into a
		 private member field of Dataset.
		 It the data does not exist at that path, then it returns an error message'''
		try:
			loaded_data = pd.read_csv(self.data_path)
		except:
			return 'incorrect path, could not find data'
		else:
			return loaded_data.shape

