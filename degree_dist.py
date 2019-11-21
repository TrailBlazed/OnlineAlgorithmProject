import matplotlib.pyplot as plt
import networkx as nx
G = nx.read_adjlist(r"D:\Online Algo\project\graphs\ijson\2013\000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.txt")
degrees=G.degree()
degree_values=sorted(set(dict(degrees).values()))
print(degree_values)
#degree_values=range(25)
histogram=[list(dict(degrees).values()).count(i)/float(nx.number_of_nodes(G)) for i in degree_values]
#plt.bar(degree_values,histogram)
plt.plot(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()


