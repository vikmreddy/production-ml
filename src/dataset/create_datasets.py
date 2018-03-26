import pandas as pd
import matplotlib as mpl
import os
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
plt.ioff() # Turn off interaction mode

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
    Delegates to an EDA object. The EDA object handles functions such
    as plotting nulls, and sends information back to the Preprocess
    object.'''
    def __init__(self, df):
        self.df = df
        self.preprocessed_df = None

    def get_preprocessed_so_far(self):
        ''' If not yet preprocessed, return the original dataframe'''
        if self.preprocessed_df == None:
            return self.df
        else:
            return self.preprocessed_df

    def fill_nulls_with_medians(self):
        ''' Currently, preprocess is not immutable. It changes state with each
        call of a particular function.'''
        if self.preprocessed_df == None:
            self.preprocessed_df = self.df
        self.preprocessed_df = self.preprocessed_df.fillna(self.preprocessed_df.median())

    def fill_nulls_with_zeros(self):
        ''' Currently, preprocess is not immutable. It changes state with each
        call of a particular function.'''
        if self.preprocessed_df == None:
            self.preprocessed_df = self.df
        self.preprocessed_df = self.preprocessed_df.fillna(0)

    def __eq__(self, other):
        # Testing if objects of the EDA class are equal or not
        # Based on: https://stackoverflow.com/questions/1227121/compare-object-instances-
        # for-equality-by-their-attributes-in-python?utm_medium=organic&utm_
        # source=google_rich_qa&utm_campaign=google_rich_qa

        # they are equal if their internal data is equal
        if self.preprocessed_df.equals(other.preprocessed_df):
            return True
        else:
            return False


class EDA(object):
    ''' Job: Runs an Exploratory Data Analysis of the data that has been
    preprocessed so far.'''
    def __init__(self, preprocessed_df, img=None):
        self.preprocessed_df = preprocessed_df
        self.image_of_plot = img

    def plot_nulls(self):
        nulls = pd.DataFrame(self.preprocessed_df.isnull().sum(),
                             columns=['nulls'])
        img = nulls.plot(kind='bar', figsize=(10,4))
        return EDA(self.preprocessed_df, img)

    def get_preprocessed_df(self):
        return self.preprocessed_df

    def __eq__(self, other):
        # Testing if objects of the EDA class are equal or not
        # Based on: https://stackoverflow.com/questions/1227121/compare-object-instances-
        # for-equality-by-their-attributes-in-python?utm_medium=organic&utm_
        # source=google_rich_qa&utm_campaign=google_rich_qa

        # they are equal if their internal data is equal
        if self.preprocessed_df.equals(other.preprocessed_df):
            return True
        else:
            return False