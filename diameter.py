import networkx as nx

def calEccentricity(G, vertex=None, shortestPath=None):
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
        return eccValue[vertex]  # return single value
    else:
        return eccValue


def diameter(G, e=None):

    if e is None:
        e=calEccentricity(G)
    return max(e.values())


if __name__=='__main__':
    G = nx.read_adjlist(r"/home/sarada/PycharmProjects/OnlineProject/000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214.txt")
    maxim=0
    for c in nx.connected_components(G):
        n=G.subgraph(c)
        l= diameter(n)
        if(maxim<l):
            maxim=l
    print("diameter:"+str(maxim))