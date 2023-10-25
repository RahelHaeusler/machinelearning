"""
1-1_MySynthData.py
"""

import sklearn.datasets as ds


# 100 data objects from two classes described by two features
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)

# output the features and the target
print(X)
print(y)

