from src.mlprod.mlapp import *

def test_instantiation():
	my_app = MachineLearningApp()
	assert my_app

def test_OCR_instantiation():
	my_app = OpticalCharacterRecognitionApp('/path/to/data', 'features_config.ini','model_config.ini')
	assert my_app

def test_dataset_instance():
	# extracts raw data from file path
	dataset = Dataset('/path/to/data')
	assert dataset

def test_features_instance():
	# config will have numcep and numcontext fields
	features = Features('features_config.ini')
	assert features

def test_model_instance():
	model = Model('model_config.ini')
	assert model