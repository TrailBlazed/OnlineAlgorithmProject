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
    G = nx.read_adjlist(r"D:\Online Algo\project\graphs\5\000000000000679c158c35a47eecb6352402baeedd22d0385b7c9d14a922f218.txt")
    maxim=0
    for c in nx.connected_components(G):
        n=G.subgraph(c)
        l= diameter(n)
        if(maxim<l):
            maxim=l
    print("diameter:"+str(maxim))