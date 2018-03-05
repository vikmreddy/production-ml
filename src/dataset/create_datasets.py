class Dataset(object):
	''' Reads raw image data, splits into lines, turns into black and white.'''
	def __init__(self, data_path):
		print(data_path)