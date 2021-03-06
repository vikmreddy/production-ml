from src.dataset.create_datasets import Dataset, Preprocess, EDA


def test_wrong_data_path():
    dataset = Dataset('/path/to/data')
    assert dataset.load_data() == 'incorrect path, could not find data'

def test_right_path_and_data_dimensions():
    dataset = Dataset('src/data/Health_data.csv')
    assert dataset.load_data() == (5148, 19)

def test_delegation_to_preprocess_object():
    dataset = Dataset('src/data/Health_data.csv')
    preprocess = Preprocess(dataset.get_data())
    assert preprocess

def test_preprocess_delegation_to_eda_object():
    '''EDA gets passed the data that has undergone preprocessing.
    In the future, I can refactor to make Preprocess
    immutable objects. So far EDA is immutable.'''
    dataset = Dataset('src/data/Health_data.csv')
    dataset.load_data()
    preprocess = Preprocess(dataset.get_data())
    eda = EDA(preprocess.get_preprocessed_so_far())
    assert eda

def test_plot_nulls_in_the_eda():
    dataset = Dataset('src/data/Health_data.csv')
    dataset.load_data()
    preprocess = Preprocess(dataset.get_data())
    eda = EDA(preprocess.get_preprocessed_so_far()).plot_nulls()
    eda_nulls = EDA(preprocess.get_preprocessed_so_far()).plot_nulls()
    assert eda == eda_nulls

def test_fill_nulls_with_medians():
    dataset = Dataset('src/data/Health_data.csv')
    dataset.load_data()
    preprocess = Preprocess(dataset.get_data())
    # First preprocess object with filled nulls
    preprocess = preprocess.fill_nulls_with_medians()
    # Another preprocess object that has filled nulls
    medians = Preprocess(dataset.get_data()).fill_nulls_with_medians()
    assert preprocess == medians

def test_fill_nulls_with_zeros():
    dataset = Dataset('src/data/Health_data.csv')
    dataset.load_data()
    preprocess = Preprocess(dataset.get_data())
    # First preprocess object with filled nulls
    preprocess = preprocess.fill_nulls_with_zeros()
    # Another preprocess object that has filled nulls
    zeros = Preprocess(dataset.get_data()).fill_nulls_with_zeros()
    assert preprocess == zeros