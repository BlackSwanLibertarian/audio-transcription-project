# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:28:21 2023

@author: raamc
"""
import matplotlib.pyplot as plt
import networkx as nx
g = nx.Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('D', 'B')

nx.draw_networkx(g, with_labels=True)

#Calculate betweenness for every node in the graph.

betweenness = nx.betweenness_centrality(g)
for node, value in betweenness.items():
    print(f"Betweenness centrality for node {node}: {value}")

nx.degree_centrality(g)
nx.closeness_centrality(g)
nx.betweenness_centrality(g)

# calculated the eigenvector centrality and will converge
ec = nx.eigenvector_centrality_numpy(g)
# ec now holds a dictionary of centrality values, lets set each node to the right value
nx.set_node_attributes(g,ec,'eigen_cent')

dc = nx.degree_centrality(g)
dc2 = [dc[x] * 1000 for x in dc]
nx.draw_networkx(g,node_size=dc2,with_labels=True)
nx.draw_networkx(g,node_color=colorarray,with_labels=True)
