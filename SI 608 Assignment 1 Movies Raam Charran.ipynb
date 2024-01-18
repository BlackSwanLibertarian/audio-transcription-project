# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:31:33 2023

@author: raamc
"""

import networkx as nx
import matplotlib.pyplot as plt      

babel = nx.read_pajek('babel.net')
pulpfiction = nx.read_pajek('pulp_fiction.net')
nx.diameter(babel)
nx.density(babel)
cliques_babel = list(nx.find_cliques(babel))
cliques_pulpfiction = list(nx.find_cliques(pulpfiction))


max_clique_size_babel = max(len(clique) for clique in cliques_babel)
biggest_cliques_babel = [clique for clique in cliques_babel if len(clique) == max_clique_size_babel]

max_clique_size_pulpfiction = max(len(clique) for clique in cliques_pulpfiction)
biggest_cliques_pulpfiction = [clique for clique in cliques_pulpfiction if len(clique) == max_clique_size_pulpfiction]

print("Biggest clique(s) in Babel:", biggest_cliques_babel, "Size:", max_clique_size_babel)
print("Biggest clique(s) in Pulp Fiction:", biggest_cliques_pulpfiction, "Size:", max_clique_size_pulpfiction)

#Number of nodes and edges:
print("Number of nodes in Babel:", babel.number_of_nodes())
print("Number of edges in Babel:", babel.number_of_edges())

print("Number of nodes in Pulp Fiction:", pulpfiction.number_of_nodes())
print("Number of edges in Pulp Fiction:", pulpfiction.number_of_edges())

#Diameter
print("Diameter of Babel:", nx.diameter(babel))
print("Diameter of Pulp Fiction:", nx.diameter(pulpfiction))

#Density

print("Density of Babel:", nx.density(babel))
print("Density of Pulp Fiction:", nx.density(pulpfiction))

#Degree
degrees_babel = dict(babel.degree())
degrees_pulpfiction = dict(pulpfiction.degree())

# For Babel graph
plt.figure(figsize=(10, 6))
plt.hist(degrees_babel.values(), bins=max(degrees_babel.values()) - min(degrees_babel.values()), edgecolor="black", color="green", alpha=0.7)
plt.title("Degree Distribution of Babel Graph")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.show()

# For Pulp Fiction graph
plt.figure(figsize=(10, 6))
plt.hist(degrees_pulpfiction.values(), bins=max(degrees_pulpfiction.values()) - min(degrees_pulpfiction.values()), edgecolor="black", color="blue", alpha=0.7)
plt.title("Degree Distribution of Pulp Fiction Graph")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.show()