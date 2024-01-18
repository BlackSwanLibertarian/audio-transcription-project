# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:38:13 2023

@author: raamc
"""

import networkx as nx
import itertools

# Step 1: Load the Karate Club graph
g = nx.karate_club_graph()

# Apply the Girvan-Newman algorithm
communities_generator = nx.algorithms.community.girvan_newman(g)

# The 'communities_generator' is now a generator object
print(communities_generator)


# Step 2: Iterate over the generator for the first k communities
k = 3  #  if you want to see the first 3 splits
for communities in itertools.islice(communities_generator, k):
    community_tuple = tuple(sorted(c) for c in communities)
    
    # Printing the community tuples
    print("community tuples:", community_tuple)
    
    # Calculating and printing the number of communities
    num_communities = len(community_tuple)
    print("number of communities:", num_communities)
    
    # Calculating and printing the size of the largest community
    max_community_size = max(len(c) for c in community_tuple)
    print("max community size:", max_community_size)
    

# Step 3: Set the limitation and apply takewhile
n = 12
limited = itertools.takewhile(lambda c: max(len(community) for community in c) >= n, communities_generator)

# Step 4: Iterate over the limited generator
for communities in limited:
    # Calculating the size of the largest community
    current_max_size = max(len(community) for community in communities)
    
    # Printing the current max size and the community tuples
    print("current max size =", current_max_size)
    print("community tuples", tuple(sorted(c) for c in communities))
