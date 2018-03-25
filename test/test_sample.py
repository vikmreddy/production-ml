from src.mlprod.mlapp import MachineLearningApp

def func(x):
	return x + 2

def test_sum_should_be_5():
	assert func(3) == 5

def test_instantiation():
	my_app = MachineLearningApp()
	assert my_app

def test_sum_should_be_7():
	assert func(5) == 7