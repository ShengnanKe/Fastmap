import pandas as pd
import numpy as np

# load data as x,y,z coordinates
pcadata = np.loadtxt('pca-data.txt')
x_data, y_data, z_data = pcadata[:, 0], pcadata[:, 1], pcadata[:, 2]

# Step - 1: Center of the data
x_mean, y_mean, z_mean = x_data.mean(), y_data.mean(), z_data.mean()
new_x_data, new_y_data, new_z_data = x_data - x_mean, y_data - y_mean, z_data - z_mean
# create the data matrix
data_matrix = np.vstack((new_x_data, new_y_data, new_z_data)).T

# Step - 2: Compute the Covariance Matrix
cov_Matrix = np.cov(data_matrix, rowvar = False)

# Step - 3: Compute the Eigenvalues and Eigenvectors
eigen_values , eigen_vectors = np.linalg.eigh(cov_Matrix)

# Step-4.1: Sort Eigenvalues in descending order
sorted_index = np.argsort(eigen_values)[::-1]
sort_eigen_value = eigen_values[sorted_index]
# Step-4.2: pair Eigenvalues with Eigenvectors
sort_eigen_vectors = eigen_vectors[:,sorted_index]

# Step - 5: select the subset from sorted eigen-vectors
# since we want to reduce the dimension to 2D dataset - selected the first two principal components
n_components = 2 
eigen_vectors_subset = sort_eigen_vectors[:,0:n_components]

# Step - 6: Constract the transformation matrix
Trans_matrix = np.dot(eigen_vectors_subset.transpose() , data_matrix.transpose() ).transpose()

#The eigen_vectors_subset represent the directions of the axis turning into
print("\n The directions of the first two principal components: \n", eigen_vectors_subset)
print("\n Dimension Reduction: 2D dataset \n",Trans_matrix)
