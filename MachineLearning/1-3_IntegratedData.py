"""
1-3_IntegratedData.py
"""

import sklearn.datasets as ds
import pandas as pd
import matplotlib
matplotlib.use('MACOSX') # On Mac the default matplotlib backend can be problematic. Choosing the backend MACOSX helps.
import matplotlib.pyplot as plt

# load an integrated data set
iris = ds.load_iris()

# with the key „data“ we have access to the features
print(iris["data"])
# with the key „target“ we have access to the target variable
print(iris["target"])
# with the key „feature_names“ we have access to the names of the features
print(iris["feature_names"])

# Create DataFrame from the data in iris.data and
# label the columns with iris.feature_names
X, f = iris["data"], iris["feature_names"]
iris_dataframe = pd.DataFrame(X, columns=f)
print(iris_dataframe)

# Erstellen einer Streudiagramm-Matrix aus dem DataFrame
y = iris["target"]
pd.plotting.scatter_matrix(iris_dataframe, c=y)

# workaround um den Plot aktiv zu halten
plt.show(block=True)