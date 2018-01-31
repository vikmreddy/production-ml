from mlapp import MachineLearningApp

def func(x):
	return x + 2

def test_sum_should_be_5():
	assert func(3) == 5

def test_instantiation():
	mlapp = new MachineLearningApp()
	assert mlapp