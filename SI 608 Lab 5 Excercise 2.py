# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:06:50 2023

@author: raamc
"""

import networkx as nx
import itertools
from networkx.algorithms.community import girvan_newman
from networkx.algorithms.community.quality import modularity
import matplotlib.pyplot as plt

#Step 1

def return_k_round_partition(g, k):
    communities_generator = girvan_newman(g)
    for i, communities in enumerate(itertools.islice(communities_generator, k)):
        if i + 1 == k:
            # Convert each community set to a list for consistency
            comm_tup = tuple(sorted(list(community)) for community in communities)
            return comm_tup

# Create the graph outside of the function so it's accessible later
g = nx.karate_club_graph()

# Define the round number for which you want the partition
k = 3  # Replace with the desired round number

#Step 2

comm_tup = return_k_round_partition(g,k)


# Compute the modularity of the partition
modularity_value = modularity(g, comm_tup)

# Output the modularity value
print("Modularity:", modularity_value)

#Step 3

#Initialize the graph
g = nx.karate_club_graph()

#Generate community partitions
communities_generator = girvan_newman(g)

#Compute modularity scores and store them
modularity_scores = []
for i, communities in enumerate(itertools.islice(communities_generator, 10)):
    partition = tuple(communities)
    score = modularity(g, partition)
    modularity_scores.append(score)
    print(f"Round {i+1}: Modularity = {score}")

#Plot the scores
rounds = range(1, 11)
plt.plot(rounds, modularity_scores, marker='o')
plt.xlabel('Rounds')
plt.ylabel('Modularity Score')
plt.title('Modularity Score vs. Rounds of Girvan-Newman Algorithm')
plt.xticks(rounds)
plt.show()

#Determine the best partition
best_round = modularity_scores.index(max(modularity_scores)) + 1
print(f"The best partition is achieved at round {best_round} with a modularity score of {max(modularity_scores)}.")
