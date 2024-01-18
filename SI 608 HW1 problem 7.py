# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:21:30 2023

@author: raamc
"""

import networkx as nx
import matplotlib.pyplot as plt


# Create a graph object
G = nx.Graph()

# Load the graph from the edge list file
file_path = 'facebook_combined.txt'
G = nx.read_edgelist(file_path)

plt.figure(figsize=(10,7))
nx.draw(G, node_size=10, edge_color='grey')
plt.show()

assortativity_score = nx.degree_assortativity_coefficient(G)

# Print the assortativity score
print("Assortativity Score:", assortativity_score)