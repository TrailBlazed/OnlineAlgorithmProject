import networkx as nx
import sys
import re
import itertools
import time


def wedge_iterator(graph,vertex=None):
    count = 0
    l=[]
    for node in graph.nbunch_iter(vertex):
        neighbors = graph.neighbors(node)
        for pair in itertools.combinations(neighbors, 2):
            yield (node, pair)
        for item in pair:
            l.append(item)
def count_triangle(graph):
    n = 0
    for wedge in wedge_iterator(graph):
        if graph.has_edge(wedge[1][0], wedge[1][1]) or graph.has_edge(wedge[1][1], wedge[1][0]):
            n += 1
    return n

if __name__ == '__main__':
    g = nx.read_adjlist(r"/home/sarada/PycharmProjects/OnlineProject/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.txt")
    print('Graph info',nx.info(g))
    n = 0
    start_time = time.time()
    n = count_triangle(g)
    w= wedge_iterator(g)
    print('Number of triangles:', n/3)
    print("Wedges count:",w)
    print('Time used:', time.time() - start_time)