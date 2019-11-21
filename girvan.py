from random import random

import networkx as nx
import collections
import pandas as pd
import matplotlib.pyplot as mtl
from networkx.algorithms.community import girvan_newman


def girvan(G):
    c= sorted(nx.connected_components(G), key = len, reverse=True)
    l=len(c)
    n= l
    print(l)
    #print('number of connected componets are:', c)
    while(n<=l):
        p=edge_to_remove(G)
        G.remove_edge(*p)
        c= sorted(nx.connected_components(G), key = len, reverse=True)
        n=len(c)
        #print(('number of connected componets are:',c))
    return c,n
def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G)
    list_of_tuples=list(dict1.items())
    list_of_tuples.sort(key=lambda tup: tup[1], reverse=True)
    x=list_of_tuples[0][0]
    return x

"""G=nx.barbell_graph(5,0)
c=girvan(G)
for i in c:
    print(i)"""

"""G=nx.karate_club_graph()
c,l=girvan(G)
print('number of connected componets are:',l)
for i in c:
    print(i)
df=pd.read_csv("/home/sarada/PycharmProjects/Online_Blockchain/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.csv",names=["s","t"])
df = df.apply(lambda x: x.astype(str))
G = nx.from_pandas_edgelist(df, source='s', target='t')
"""
G= nx.read_adjlist(r"D:\Online Algo\project\graphs\ijson\0000000000000a3290f20e75860d505ce0e948a1d1d846bec7e39015d242884b.txt")
c,l=girvan(G)


print('Number of connected componets are:',l)
"""
for i in c:
    print(i)
nx.draw(G,node_size=5)
mtl.show()
"""
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
