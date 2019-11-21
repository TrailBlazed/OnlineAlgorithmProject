from random import random

import networkx as nx
import collections
import pandas as pd
import matplotlib.pyplot as mtl
from networkx.algorithms.community import girvan_newman


def girvan(G):
    conn_comp= sorted(nx.connected_components(G), key = len, reverse=True)
    l=len(conn_comp)
    n= l
    print(l)
    #print('number of connected componets are:', c)
    while(n<=l):
        p=edge_to_remove(G)
        G.remove_edge(*p)
        conn_comp= sorted(nx.connected_components(G), key = len, reverse=True)
        n=len(conn_comp)
        #print(('number of connected componets are:',c))
    return conn_comp,n
def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G)
    list_of_tuples=list(dict1.items())
    list_of_tuples.sort(key=lambda tup: tup[1], reverse=True)
    x=list_of_tuples[0][0]
    return x
G= nx.read_adjlist(r"D:\Online Algo\project\graphs\ijson\0000000000000a3290f20e75860d505ce0e948a1d1d846bec7e39015d242884b.txt")
c,l=girvan(G)


print('Number of connected componets are:',l)
#assing cluster colours
colors = [(random(), random(), random()) for _i in range(l)]
nodes = list(G.nodes)
nodeColor = []
for node in nodes:
    for x in range(0, len(c)):
        if c[x].__contains__(node):
            nodeColor.append(colors[x])

print(nodeColor)
nx.draw(G,node_color=nodeColor, node_size =5)
mtl.show()
