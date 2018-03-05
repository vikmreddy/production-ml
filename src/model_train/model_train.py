class ModelTrain():
	''' Model Train has a Read Data object.
	The read data object will have raw data as well as the cleaned data lines.
	These lines will be then processed by read data to end up with rows of pixels.'''
	def __init__(self, Read_Data):
		self.read_data = Read_Data
