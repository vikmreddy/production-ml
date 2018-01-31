class MachineLearningApp(object):
	''' Base class for all Machine Learning Applications'''
	def __init__(self):
		self.Train = None
		self.Read_Dataset = None

class OpticalCharacterRecogApp(MachineLearningApp):
	''' App for Optical Character Recognition (OCR) for English and
	Foreign Languages '''
