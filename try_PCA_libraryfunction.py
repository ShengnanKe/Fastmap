import pandas as pd
from sklearn.decomposition import PCA

# Importing the dataset
dataset = pd.read_csv('pca-data.txt', delim_whitespace = True, header = None)

dataset_reduced = PCA(n_components=2).fit_transform(dataset)
print(dataset_reduced)
