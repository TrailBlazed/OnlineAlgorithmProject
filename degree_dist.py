import matplotlib.pyplot as plt
import networkx as nx

# Read the adjacency list for the bitcoin network graph are undirected graph
G = nx.read_adjlist(r"D:\Online Algo\project\graphs\ppt\0000000000000751db4fb6228b0b53898c70d5972623e6016e90261e45b694a2.txt")
# G= nx.read_adjlist(r"D:\Online Algo\project\graphs\actor imdb\actor.csv" , delimiter=',', encoding='cp1252')

# Calculate the fraction of nodes having a given degree
degrees=G.degree()
degree_values=sorted(set(dict(degrees).values()))
histogram=[list(dict(degrees).values()).count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

# Plot the degree distribution result
plt.figure()
ax2 = plt.axes()
my_ticks = [i for i in range(len(degree_values))]
ax2.set_xticks(my_ticks)
ax2.set_xticklabels(degree_values)
ax2.plot(my_ticks, histogram)
ax2.set_title('Degree distribution')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()





