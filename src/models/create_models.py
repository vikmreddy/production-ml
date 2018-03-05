class Model(object):
	'''Is an abstract class to define the Deep Learning model.
	Implemented Types:
		LSTM
		BLSTM
		CNN
	'''
	def __init__(self, config):
		self.config = config
	