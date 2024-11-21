import pandas as pd
# Load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
# Cleaning data
def sum_nan(data):
    return data.isna().sum()

def usera_nan(data):
    idx = data[data['user_b'].isnull()].index.tolist()
    usera_nan = data['user_a'][idx].values
    return usera_nan, idx
def fill_values(data, idx, values):
    data.loc[idx, 'user_b'] = values
    return data
