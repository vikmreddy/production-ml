class MachineLearningApp(object):
	''' Base class for all Machine Learning Applications'''
	def __init__(self):
		self.Train = None
		self.Read_Dataset = None

class OpticalCharacterRecognitionApp(MachineLearningApp):
	''' App for Optical Character Recognition (OCR) for English and
	Foreign Languages.

	Delegation:
	Dataset object reads dataset, does image preprocessing, extracts lines,
		and partitions into train, dev, and test.
	Features object extracts features from the lines of text.
	Train object runs the model.
	Test object runs the model against test data.'''

	def __init__(self):
		# Composition, self contains other objects
		self.Dataset = None
		self.Features = None
		self.Model = None
		self.Train = None
		self.Eval = None

