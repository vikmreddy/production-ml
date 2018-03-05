from src.dataset.create_datasets import Dataset
from src.features.create_features import Features
from src.models.create_models import Model

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

	def __init__(self, data_path, features_config, model_config):
		# Composition, self contains other objects
		self.Dataset = Dataset(data_path)
		self.Features = Features(features_config)
		self.Model = Model(model_config)
		self.Train = None
		self.Eval = None

