import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes with degree')
    bins_edge=range(25)
    plt.hist(degrees,bins=bins_edge)
    plt.show()
G = nx.read_adjlist(r"/home/sarada/PycharmProjects/OnlineProject/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.txt")
plot_degree_dist(G)
print(len(G.nodes()))

#list(dict(nx.degree(G)).values())