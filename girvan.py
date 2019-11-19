import networkx as nx
import collections
import pandas as pd
import matplotlib as mtl
def girvan(G):
    c= sorted(nx.connected_components(G), key = len, reverse=True)
    l=len(c)
    #print('number of connected componets are:', c)
    while(l==1):
        p=edge_to_remove(G)
        G.remove_edge(*p)
        c= sorted(nx.connected_components(G), key = len, reverse=True)
        l=len(c)
        #print(('number of connected componets are:',c))
    return c,l
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
    print(i)"""
df=pd.read_csv("/home/sarada/PycharmProjects/Online_Blockchain/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.csv",names=["s","t"])
df = df.apply(lambda x: x.astype(str))
G = nx.from_pandas_edgelist(df, source='s', target='t')

c,l=girvan(G)


print('Number of connected componets are:',l)
for i in c:
    print(i)
nx.draw(G, node_color=list(c.values()))
mtl.show()
