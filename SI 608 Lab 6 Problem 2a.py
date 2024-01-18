# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:31:20 2023

@author: raamc
"""

import networkx as nx
import random

# Seed for reproducibility
random.seed(2666)

# 0. Generate an ER graph with n=100 nodes, p=0.05 probability, and seed=2666
G_er = nx.erdos_renyi_graph(n=100, p=0.05, seed=2666)

# 1. Function to fetch the most valuable edge based on betweenness centrality
def fetch_most_valuable_edge(g):
    betweenness = nx.edge_betweenness_centrality(g)
    return max(betweenness, key=betweenness.get)

# 2. Function to perform one iteration of betweenness clustering
def perform_betw_clustering(g, fetch_edge):
    if g.number_of_edges() == 0:
        return list(nx.connected_components(g))
    
    g_cp = g.copy().to_undirected()
    g_cp.remove_edges_from(nx.selfloop_edges(g_cp))
    initial_num_components = nx.number_connected_components(g_cp)
    
    while g_cp.number_of_edges() > 0:
        edge = fetch_edge(g_cp)
        g_cp.remove_edge(*edge)
        
        new_num_components = nx.number_connected_components(g_cp)
        if new_num_components > initial_num_components:
            break
    
    return sorted(list(nx.connected_components(g_cp)), key=len, reverse=True)

# Example of performing one iteration of betweenness clustering
communities = perform_betw_clustering(G_er, fetch_most_valuable_edge)
for community in communities:
    print(sorted(community))

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
