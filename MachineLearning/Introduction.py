import sklearn.datasets as ds
import matplotlib.pyplot as plt

# 100 data objects from two classes described by two features
# X = features, y = target (class)
# synthetic data means: creating random data
# n_samples = number of samples, n_features = number of features (attribute)
# n_redundant = don't want to have repetition of data, n_classes = number of classification
# (binary classification if only 2 classes requested)
# x = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)
# output the features and the target
print(X)
print(y)