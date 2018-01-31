from src.mlprod.mlapp import *

def test_instantiation():
	my_app = MachineLearningApp()
	assert my_app

def test_OCR_instantiation():
	my_app = OpticalCharacterRecognitionApp()
	assert my_app