# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here

def data_splitter(df):
    y = df['SalePrice']
    #X = df.drop(columns=['SalePrice'])
    X = df.drop('SalePrice', axis=1)
    return X,y





