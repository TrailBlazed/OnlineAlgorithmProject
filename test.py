import networkx as nx
from girvan import get_girvan_and_plot
from diameter import get_diameter
from triangle_triadic import get_triangle_triadic
from degree_dist import degree_distr
from Address_Graph import get_block_data_early, get_block_data_latest

# Getting the data from the Block
result, path = get_block_data_early(r"D:\Online Algo\project\graphs\latest","0000000000000a3290f20e75860d505ce0e948a1d1d846bec7e39015d242884b", 3)

# Creating a Bitcoin graph object from adjacency list stored in file
G = nx.read_adjlist(path)

# Calling community detection algorithm in Bitcoin graph
get_girvan_and_plot(G)

#Calculating the Bitcoin graph diameter
result1, dia = get_diameter(G)
print("Diameter: ",dia)

#Calulating the triangle density and triadic closure
result2, tridens, triadic = get_triangle_triadic(G)
print("Triangle density : ",tridens)
print("Triadic closure : ",tridens)

# Degree distribution of the Bitcoin graph
print(degree_distr(G))
