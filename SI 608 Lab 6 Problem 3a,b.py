# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:21:03 2023

@author: raamc
"""

import networkx as nx

# Full path to 'email-Eu-core.txt' on your system
file_path = r'C:\Users\raamc\OneDrive\Desktop\Projects\email-Eu-core.txt'

# Load the graph
G = nx.read_edgelist(file_path, create_using=nx.Graph(), nodetype=int)

# Convert to undirected graph (if it's not already)
G = G.to_undirected()

# Print out graph information
print(G)


# Find communities using the Clauset-Newman-Moore greedy modularity maximization
communities = list(nx.algorithms.community.greedy_modularity_communities(G))

# Report the number of communities found
num_communities = len(communities)
print(f"Number of communities found: {num_communities}")

# Find the largest community by number of nodes
largest_community_size = max(len(community) for community in communities)
print(f"Number of nodes in the largest community: {largest_community_size}")

import networkx as nx
from itertools import combinations

# Assuming you have already found communities using modularity-based clustering and stored them in `communities`

# Path to the ground truth file
ground_truth_path = r'C:\Users\raamc\OneDrive\Desktop\Projects\email-Eu-core-department-labels.txt'

# Load the ground truth communities
ground_truth_communities = {}
with open(ground_truth_path, 'r') as file:
    for line in file:
        node, community = line.strip().split()
        node, community = int(node), int(community)
        if community in ground_truth_communities:
            ground_truth_communities[community].add(node)
        else:
            ground_truth_communities[community] = {node}

# Report the number of communities in ground truth
print(f"Number of communities in ground-truth: {len(ground_truth_communities)}")

# Function to compute pairwise accuracy
def compute_accuracy(detected, ground_truth):
    detected_pairs = set()
    for community in detected:
        detected_pairs.update(combinations(community, 2))

    ground_truth_pairs = set()
    for community in ground_truth.values():
        ground_truth_pairs.update(combinations(community, 2))

    intersection = len(detected_pairs & ground_truth_pairs)
    total_pairs = len(detected_pairs | ground_truth_pairs)
    
    accuracy = intersection / total_pairs if total_pairs > 0 else 0
    return accuracy

# Compute the accuracy
accuracy = compute_accuracy(communities, ground_truth_communities)
print(f"Accuracy of pairwise community memberships: {accuracy}")
