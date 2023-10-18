import sklearn.datasets as ds
import matplotlib.pyplot as plt

X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)

# output the data set with a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Data Set with 100 Data Objects, 2 Features, 2 Classes')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()
