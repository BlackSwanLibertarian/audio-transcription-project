# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:29:42 2023

@author: raamc
"""

import networkx as nx
import numpy as np

# Load the graph from the specified path
g = nx.read_gml(r'C:\Users\raamc\OneDrive\Desktop\Projects\p3_graph.gml')

# Map node labels to indices
node_to_index = {node: i for i, node in enumerate(g.nodes())}

# Initialize the transition matrix with zeros
tran_matrix = np.zeros((len(g), len(g)))

# Construct the transition matrix
for node_i in g.nodes():
    out_degree_i = g.out_degree(node_i)
    if out_degree_i > 0:
        for node_j in g.neighbors(node_i):
            # Use the mapping to find indices for the matrix
            index_i = node_to_index[node_i]
            index_j = node_to_index[node_j]
            tran_matrix[index_i][index_j] = 1 / out_degree_i

# Print the transition matrix
print(tran_matrix)

import numpy as np

def iterate_state_dis(state_dis, tran_matrix):
    # Initialize the previous distribution to compare later for convergence
    prev_state_dis = np.zeros_like(state_dis)

    # Initialize step count
    step_count = 0

    # Iterate until convergence
    while True:
        # Update the state distribution
        new_state_dis = np.dot(tran_matrix.T, state_dis)
        
        # Check for convergence using the infinity norm for the difference
        if np.linalg.norm(new_state_dis - prev_state_dis, np.inf) < 1e-5:
            break
        
        # Update the previous distribution and increase the step count
        prev_state_dis = new_state_dis
        step_count += 1

    return new_state_dis, step_count

# Calculate the stationary distribution and report the step of iteration

# Define the initial state distribution (uniform distribution)
state_dis = np.full((len(g), 1), 1/len(g))

# Get the stationary distribution and step count
stationary_dis_b, step_count = iterate_state_dis(state_dis, tran_matrix)

# Report the step
print(f'It took {step_count} steps to converge.')

import numpy as np

# Assume 'tran_matrix' is your transition matrix defined previously

# 1. Get the eigenvectors and eigenvalues for the transpose of the transition matrix
eig_vals, eig_vecs = np.linalg.eig(tran_matrix.T)

# 2. Print the eigenvalues to find "1"
print(eig_vals)

# 3. Get the corresponding eigenvector for the eigenvalue 1
# We find the index where the eigenvalue is closest to 1
index_of_one = np.argmin(np.abs(eig_vals - 1))
stationary_dis_c = eig_vecs[:, index_of_one]

# 4. We need to scale the vector to make sure all values are real and non-negative and the sum is 1
stationary_dis_c = np.real(stationary_dis_c)
stationary_dis_c = stationary_dis_c / np.sum(stationary_dis_c)

# 5. Report the difference
print(stationary_dis_c)
