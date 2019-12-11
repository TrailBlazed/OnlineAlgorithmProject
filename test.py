import networkx as nx
from girvan import get_girvan_and_plot
from diameter import get_diameter
from triangle_density import get_triangle_density
from degree_dist import degree_distr
from Address_Graph import get_block_data_early, get_block_data_latest

#result, path = get_block_data_latest(r"D:\Online Algo\project\graphs\latest",3)
result, path = get_block_data_early(r"D:\Online Algo\project\graphs\latest","0000000000000a3290f20e75860d505ce0e948a1d1d846bec7e39015d242884b", 3)

G = nx.read_adjlist(path)

get_girvan_and_plot(G)

result1, dia = get_diameter(G)
print("Diameter: ",dia)

result2, tridens = get_triangle_density(G)
print("Triangle density : ",tridens)

degree_distr(G)
