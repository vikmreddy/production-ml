import pandas as pd

class Dataset(object):
    ''' Job: Reads raw data, delegates to preprocess and EDA functions.'''
    def __init__(self, data_path):
        self.data_path = data_path
        self.loaded_data = None

    def load_data(self):
        ''' Loads data from data path and returns the dimensions of that dataset.
         It verifies if the data path exists or not. If it does, it returns the
         dimensions of the data at that location. It also loads the data into a
         private member field of Dataset.
         It the data does not exist at that path, then it returns an error message'''
        try:
            self.loaded_data = pd.read_csv(self.data_path)
        except:
            return 'incorrect path, could not find data'
        else:
            return self.loaded_data.shape

    def get_data(self):
        return self.loaded_data

class Preprocess(object):
    ''' Job: Preprocesses data and sends it back to the Dataset object.
    Delagates to an EDA object. The EDA object handles functions such
    as plotting nulls, and sends information back to the Preprocess
    object.'''
    def __init__(self, df):
        self.df = df
        self.preprocessed_df = None

    def get_preprocessed_so_far(self):
        return self.preprocessed_df

class EDA(object):
    ''' Job: Runs an Exploratory Data Analysis of the data that has been
    preprocessed so far.'''
    def __init__(self, preprocessed_df):
        self.preprocessed_df = preprocessed_df
