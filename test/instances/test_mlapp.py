from src.mlprod.mlapp import *

def test_instantiation():
    my_app = MachineLearningApp()
    assert my_app

def test_structured_data_instantiation():
    my_app = StructuredDataApp('/path/to/data',
                               'features_config.ini',
                               'model_config.ini')
    assert my_app

def test_dataset_instance():
    dataset = Dataset('/path/to/data')
    assert dataset

def test_features_instance():
    features = Features('features_config.ini')
    assert features

def test_model_instance():
    model = Model('model_config.ini')
    assert model