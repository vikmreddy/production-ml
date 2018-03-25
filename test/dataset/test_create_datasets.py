from src.dataset.create_datasets import Dataset

def test_wrong_data_path():
    dataset = Dataset('/path/to/data')
    assert dataset.load_data() == 'incorrect path, could not find data'