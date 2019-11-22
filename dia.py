import networkx as nx
def eccentricity(G, v=None, sp=None):
    order = G.order()
    e = {}
    for n in G.nbunch_iter(v):
        if sp is None:
            length = nx.single_source_shortest_path_length(G, n)
            L = len(length)
        else:
            try:
                length = sp[n]
                L = len(length)
            except TypeError:
                raise nx.NetworkXError('Format of "sp" is invalid.')
        if L != order:
            msg = "Graph not connected: infinite path length"
            raise nx.NetworkXError(msg)

        e[n] = max(length.values())

    if v in G:
        return e[v]  # return single value
    else:
        return e
def diameter(G, e=None):

    if e is None:
        e=eccentricity(G)
    return max(e.values())
if __name__=='__main__':
    G = nx.Graph()
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_node("D")
    G.add_node("E")
    G.add_node("F")
    G.add_node("G")
    G.add_edge("A","B")
    G.add_edge("B","C")
    G.add_edge("B","D")
    G.add_edge("E","F")
    G.add_edge("F","G")
    G.add_edge("G","H")
    max=0
    for c in nx.connected_components(G):
        n=G.subgraph(c)
        eccentricity(n)
        l=diameter(n)
        print(l)
        if(max<l):
            max=l
    print(max)