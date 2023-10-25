"""
1-4_ExternalData.py
"""

import pandas as pd

# .csv file has no header that names the columns, so we pass
# header=None and explicitly specify the column names in "names".
data = pd.read_csv('census.data', header=None, index_col=False,
                   names=['age', 'workclass', 'fnlwgt',
                            'education', 'education-num', 'marital- status', 'occupation',
                            'relationship', 'race', 'gender', 'capital-gain',
                            'capital-loss', 'hours-per-week', 'native-country', 'income'])

# manually select some columns from a DataFrame
reduced_data = data[['age', 'workclass', 'education', 'income']]

# Output the data
print(reduced_data)

# using loc() to extract a slice of the DataFrame by specify start and end features.
# Note that contrary to usual python slices, both, the start and the stop are included!
data_input = data.loc[:, 'age':'native-country']  # we use it here to extract all the input variables
print(data_input)  # the output is a data frame

# Extract all input variables from the DataFrame using loc
# and convert them to a NumPy array using values.
data_input_num = data.loc[:, 'age':'native-country'].values
print(data_input_num)  # the output is a numpy array

data_target_num = data[["income"]].values
print(data_target_num)
