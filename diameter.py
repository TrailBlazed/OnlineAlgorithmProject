import networkx as nx

def calDiameter(G, vertex=None, shortestPath=None):
    # calculating diameter
    order = G.order()
    eccValue = {}
    for n in G.nbunch_iter(vertex):
        if shortestPath is None:
            length = nx.single_source_shortest_path_length(G, n)
            L = len(length)
        else:
            try:
                length = shortestPath[n]
                L = len(length)
            except TypeError:
                raise nx.NetworkXError('Format of "sp" is invalid.')
        if L != order:
            msg = "Graph not connected: infinite path length"
            raise nx.NetworkXError(msg)

        eccValue[n] = max(length.values())

    if vertex in G:
        return max(eccValue[vertex].values())# return single value
    else:
        return max(eccValue.values())


def get_diameter(netwgraph):
    # calculating diameter of all the subgraphs and returning the maximum value
    maxim = 0
    try:
        for c in nx.connected_components(netwgraph):
            subgrph = netwgraph.subgraph(c)
            diamt = calDiameter(subgrph)
            if (maxim < diamt):
                maxim = diamt
    except Exception as e:
        return "Fail", e
    return "Success",maxim

