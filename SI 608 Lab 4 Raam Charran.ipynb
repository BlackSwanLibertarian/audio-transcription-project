# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:35:13 2023

@author: raamc
"""

import networkx as nx
import itertools

g = nx.karate_club_graph()

# Girvan-Newman algorithm to get communities
communities_generator = nx.algorithms.community.girvan_newman(g)

# To get the first level of communities
first_level_communities = next(communities_generator)
first_level_communities = [list(community) for community in first_level_communities]

# Display the first level of communities
print("First level communities: ", first_level_communities)

# Step 2

# Initialize the Girvan-Newman algorithm
communities_generator = nx.algorithms.community.girvan_newman(g)

k = 3  # The number of community structures you want to explore
for communities in itertools.islice(communities_generator, k):
    # Convert each community set to a list and then create a tuple of these lists
    community_tuple = tuple(sorted(c) for c in communities)
    
    # Display the community tuple
    print("community tuples:", community_tuple)
    
    # Display the number of communities
    num_communities = len(community_tuple)
    print("number of communities:", num_communities)
    
    # Display the size of the largest community
    max_community_size = max(len(community) for community in community_tuple)
    print("max community size:", max_community_size)
    
#Step 3

# Initialize the Girvan-Newman algorithm
communities_generator = nx.algorithms.community.girvan_newman(g)

n = 12  # Set the limit for the maximum community size

# Apply takewhile() to stop when max community size is less than n
limited = itertools.takewhile(lambda communities: max(len(community) for community in communities) >= n, communities_generator)

for communities in limited:
    # Get the maximum community size in the current communities set
    current_max_size = max(len(community) for community in communities)
    
    # Display the current max size
    print("current max size =", current_max_size)
    
    # Convert communities to tuple of sorted lists and display
    community_tuple = tuple(sorted(c) for c in communities)
    print("community tuples:", community_tuple)


# Excercise 2

import itertools
import networkx as nx

def return_k_round_partition(k):
    # Load the Karate Club graph
    g = nx.karate_club_graph()
    
    # Initialize the Girvan-Newman algorithm
    communities_generator = nx.algorithms.community.girvan_newman(g)
    
    # Skip to the k-th partition using itertools.islice
    for i, communities in enumerate(itertools.islice(communities_generator, k)):
        # Convert each set of communities to a tuple of sorted lists
        comm_tup = tuple(sorted(c) for c in communities)
        
    return comm_tup

# Step 2
from networkx.algorithms.community.quality import modularity
import networkx as nx

# Define your return_k_round_partition function or load comm_tup some other way
def return_k_round_partition(k):
    g = nx.karate_club_graph()
    communities_generator = nx.algorithms.community.girvan_newman(g)
    for i, communities in enumerate(itertools.islice(communities_generator, k)):
        comm_tup = tuple(sorted(c) for c in communities)
    return comm_tup

# Load the Karate Club graph
g = nx.karate_club_graph()

# Get the 3rd round partition
k = 3
comm_tup = return_k_round_partition(k)

# Compute the modularity score
mod_score = modularity(g, comm_tup)
print("Modularity Score:", mod_score)
