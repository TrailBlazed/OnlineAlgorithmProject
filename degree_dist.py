import matplotlib.pyplot as plt
import networkx as nx


def degree_distr(netwgraph):
    try:
        # Calculate the fraction of nodes having a given degree
        degrees = netwgraph.degree()
        degree_values = sorted(set(dict(degrees).values()))
        histogram = [list(dict(degrees).values()).count(i) / float(nx.number_of_nodes(netwgraph)) for i in degree_values]

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
    except Exception as e:
        return e
    return 'Success'


