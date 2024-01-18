# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:52:05 2023

@author: raamc
"""
import networkx as nx

g = nx.Graph()
g.add_edge('a', 'b')  # this will create two nodes AND an edge
g.add_edge('b', 'c')
g.add_edge('a', 'c')
g.add_edge('c', 'd')

import matplotlib.pyplot as plt      # you only need to do this once
nx.draw_networkx(g) # to draw the graph
plt.show()  # to force it to draw to the screen
nx.draw_networkx(g, with_labels=False)  # draw graph with node labels
print (nx.shortest_path(g,'a','d'))
g.add_node(1)   # this adds a node with the name “1”
g.add_nodes_from([2,3])
g.remove_node(2)
g.add_edge('a',1)
nx.draw_networkx(g, with_labels=True)  # draw graph with node labels

float(g.number_of_edges())
float(g.number_of_nodes())
mean_edges_per_node = float(g.number_of_edges()) / g.number_of_nodes()
print(mean_edges_per_node)

for node in g.nodes():
    print(node, g.degree(node))
    

degree = g.degree()    
degreevals = [val for (node, val) in degree]
degvaluniq = sorted(set(degreevals))
hist = [degreevals.count(x) for x in degvaluniq]   
plt.figure()
plt.plot(degvaluniq,hist,'ro-')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.show()

degree = g.degree()    
degreevals = [val for (node, val) in degree]

plt.hist(degreevals,bins=range(0,5), rwidth=1,align='left') #use matplotlib histogram function

plt.xlabel("Degree")

plt.ylabel("Number of nodes")

nx.is_connected(g)
nx.connected_components(g)
[comp for comp in nx.connected_components(g)]