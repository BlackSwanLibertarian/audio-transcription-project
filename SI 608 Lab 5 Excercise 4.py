# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:16:58 2023

@author: raamc
"""

import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import random
import copy
from collections import Counter

# Create a Barabási-Albert graph
gr = nx.barabasi_albert_graph(100, 3, seed=2666)

# Color map
val_map = {0: "ghostwhite",       # white: uninfected
           1: "lightcoral",       # red: infected
           2: "lightsteelblue",   # blue: infected
           3: "wheat"}            # yellow: uninfectable

# Set all nodes to be uninfected
original_state = {n: 0 for n in gr.nodes()}
nx.set_node_attributes(gr, original_state, "infected_status")

# Make nodes 5 and 2 red (infected status 1)
for node in [5, 2]:
    gr.nodes[node]["infected_status"] = 1

# Make nodes 14 and 19 blue (infected status 2)
for node in [14, 19]:
    gr.nodes[node]["infected_status"] = 2

# Make node 13 yellow (inoculated, status 3)
gr.nodes[13]["infected_status"] = 3

# Draw the graph
colors = [val_map[gr.nodes()[n]["infected_status"]] for n in gr.nodes()]
plt.figure(figsize=(12, 8))  # Set the size of the figure
nx.draw(gr, node_color=colors, edge_color="k", with_labels=True)
plt.show()

def run_simulation(grph):
    changed = True  # flag to check if any node's status changed in the last iteration
    while changed:
        changed = False  # reset the flag
        new_state = copy.deepcopy(nx.get_node_attributes(grph, "infected_status"))  # create a copy of the current state

        for n in grph.nodes():
            if new_state[n] == 0:  # if uninfected
                neighbors_status = [grph.nodes[neighbor]["infected_status"] for neighbor in grph.neighbors(n)]
                infected_neighbors = [status for status in neighbors_status if status in [1, 2]]

                if infected_neighbors:  # if there are any infected neighbors
                    status_counts = Counter(infected_neighbors)
                    # Determine the majority color, in case of a tie, pick randomly between the two
                    majority_status = status_counts.most_common(1)[0][0] if len(status_counts) == 1 else random.choice([1, 2])
                    new_state[n] = majority_status
                    changed = True  # a node's status changed, so we will need another iteration

        # Update the graph with the new states
        nx.set_node_attributes(grph, new_state, "infected_status")

    # Count the final totals
    final_states = list(nx.get_node_attributes(grph, "infected_status").values())
    total1 = final_states.count(1)  # number of nodes infected by the first campaign
    total2 = final_states.count(2)  # number of nodes infected by the second campaign
    print("Diffusion ended with", total1, "nodes infected with red and", total2, "nodes infected with blue.")

# Function to set the initial states (this needs to be implemented)
def setnodes(gr):
    # Set some nodes as infected by 1, some by 2, and some as inoculated
    # This is an example and should be replaced with your specific initialization logic
    original_state = {n: random.choice([0, 1, 2, 3]) for n in gr.nodes()}
    nx.set_node_attributes(gr, original_state, "infected_status")

# Function to create a network, set initial states, and run the diffusion model.
def runSimulations(node, edge):
    for i in range(1, 10):
        print("Run:", i)
        gr = nx.barabasi_albert_graph(node, edge)
        setnodes(gr)  # You need to implement this to initialize the infected_status correctly
        run_simulation(gr)

runSimulations(100, 3)
