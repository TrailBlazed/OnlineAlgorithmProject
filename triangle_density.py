import networkx as nx
"""G=nx.Graph()
G.add_edge("A","B")
G.add_edge("B","C")
G.add_edge("A","C")"""
G = nx.read_adjlist(r"/home/sarada/PycharmProjects/OnlineProject/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.txt")
all_cliques= nx.enumerate_all_cliques(G)
triangles=[x for x in all_cliques if len(x)==3 ] #all cliques (k=1,2,3...max degree - 1)
t=(len(triangles))
path_lengths = nx.all_pairs_shortest_path_length(G)
g=dict(nx.all_pairs_shortest_path_length(G))
print(g)
count=0
for i in g:
    for j in g[i]:
        if(g[i][j]==2):
            count=count+1
            print("length between",i,"and",j," is ",g[i][j])

print("Number of Wedges: ",count)
print("Number of Triangles: ",t)
triangle_density= (3*t)/count
print("Triangle density:",triangle_density)

