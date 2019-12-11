from random import random
import networkx as nx
import matplotlib.pyplot as mtl


def girvan_community(netwgraph):
    # forming community
    conn_comp = sorted(nx.connected_components(netwgraph), key=len, reverse=True)
    num_comp = len(conn_comp)
    num_comp_after = num_comp

    while num_comp_after <= num_comp:
        p = edge_to_remove(netwgraph)
        netwgraph.remove_edge(*p)
        conn_comp = sorted(nx.connected_components(netwgraph), key=len, reverse=True)
        num_comp_after = len(conn_comp)

    return conn_comp, num_comp_after


def edge_to_remove(G):
    # get the edge to be removed according to the betweennness
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = list(dict1.items())
    list_of_tuples.sort(key=lambda tup: tup[1], reverse=True)

    # get edge with highest betweenness
    remove_edge = list_of_tuples[0][0]
    return remove_edge


def get_girvan_and_plot(G):
    try:
        con_comp, n_con_comp = girvan_community(G)

        # assign colors to each node depending upon its community
        colors = [(random(), random(), random()) for _i in range(n_con_comp)]
        all_nodes = list(G.nodes)
        node_Color = []
        for node in all_nodes:
            for x in range(0, len(con_comp)):
                if con_comp[x].__contains__(node):
                    node_Color.append(colors[x])

        nx.draw(G, node_color=node_Color, node_size=5)
        mtl.show()
    except Exception as e:
        return e
    return "Success"


if __name__ == '__main__':
    G = nx.read_adjlist(
        r"D:\Online Algo\project\graphs\ijson\000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506.txt")
    print(get_girvan_and_plot(G))