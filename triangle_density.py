import networkx as nx
import itertools


def wedge_iterator(graph, vertex=None):
    # calculating all the wedges
    for node in graph.nbunch_iter(vertex):
        neighbors = graph.neighbors(node)
        for pair in itertools.combinations(neighbors, 2):
            yield (node, pair)


def count_triangle(graph):
    # counting all the wedges of all the triangles ( 3 * number of triangles )
    n = 0
    for wedge in wedge_iterator(graph):
        if graph.has_edge(wedge[1][0], wedge[1][1]) or graph.has_edge(wedge[1][1], wedge[1][0]):
            n += 1
    return n


def get_triangle_density(netxgraph):
    # calculating triangle density and triadic closure of the graph ((3 * number of triangles)/(number of wedges))
    triangle_density = 0
    try:
        # removing self loops
        netxgraph.remove_edges_from(nx.selfloop_edges(netxgraph))

        n_traingle_wedges = count_triangle(netxgraph)
        wedges = [n for n in wedge_iterator(netxgraph)]
        n_wedges = len(wedges)
        if n_traingle_wedges != 0:
            # calculating triangle density if there exists any triangle
            triangle_density = n_traingle_wedges / n_wedges
        triad = nx.average_clustering(netxgraph)

    except Exception as e:
        return "Fail", e
    return "Success", triangle_density, triad
