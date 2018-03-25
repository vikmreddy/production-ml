from src.dataset.create_datasets import Dataset

def test_wrong_data_path():
    dataset = Dataset('/path/to/data')
    assert dataset.load_data() == 'incorrect path, could not find data'

def test_right_path_and_data_dimensions():
    dataset = Dataset('src/data/Health_data.csv')
    assert dataset.load_data() == (5148, 19)