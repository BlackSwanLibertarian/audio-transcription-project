# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:17:30 2023

@author: raamc
"""

import networkx as nx
import random

# Seed for reproducibility
random.seed(2666)

# Generate an ER graph
G_er = nx.erdos_renyi_graph(n=100, p=0.05, seed=2666)

# Function to get the most valuable edge
def fetch_most_valuable_edge(g):
    betweenness = nx.edge_betweenness_centrality(g)
    return max(betweenness, key=betweenness.get)

# Function to perform betweenness clustering for a given number of rounds
def betweenness_clustering(g, fetch_edge, num_rounds=3):
    # Perform the clustering and record the metrics
    for _ in range(num_rounds):
        # Perform one round of betweenness clustering
        community_list = perform_betw_clustering(g, fetch_edge)
        
        # Calculate the modularity score
        modularity_score = nx.algorithms.community.modularity(g, community_list)
        
        # Record the metrics
        detected_communities = [list(community) for community in community_list]
        num_communities = len(community_list)
        max_community_size = max(map(len, community_list))
        
        # Print the metrics for the current round
        print(f"Detected communities: {detected_communities}")
        print(f"Number of communities: {num_communities}")
        print(f"Max community size: {max_community_size}")
        print(f"Modularity score: {modularity_score}\n")
        
        # Remove the most valuable edge for the next round
        if g.number_of_edges() > 0:
            edge_to_remove = fetch_edge(g)
            g.remove_edge(*edge_to_remove)

# Execute the function
betweenness_clustering(G_er, fetch_most_valuable_edge)
