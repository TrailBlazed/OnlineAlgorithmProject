import networkx as nx

"""def diameter(self):
    
    v = self.vertices()
    pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
    smallest_paths = []
    for (s, e) in pairs:
        paths = self.find_all_paths(s, e)
        smallest = sorted(paths, key=len)[0]
        smallest_paths.append(smallest)

    smallest_paths.sort(key=len)

    # longest path is at the end of list, 
    # i.e. diameter corresponds to the length of this path
    diameter = len(smallest_paths[-1]) - 1
    return diameter
graph = nx.karate_club_graph()

diameter = graph.diameter()

print(diameter)"""


def longest_path(G):
    dist = {} # stores [node, distance] pair
    for node in nx.topological_sort(G):
        # pairs of dist,node for all incoming edges
        pairs = [(dist[v][0]+1,v) for v in G.pred[node]]
        if pairs:
            dist[node] = max(pairs)
        else:
            dist[node] = (0, node)
    node,(length,_)  = max(dist.items(), key=lambda x:x[1])
    path = []
    while length > 0:
        path.append(node)
        length,node = dist[node]
    return list(reversed(path))

if __name__=='__main__':
    G = nx.DiGraph()
    G.add_edge("1","2")
    G.add_edge("2","3")
    G.add_edge("1","3")
    G.add_edge("4", "1")
#    G.add_path([20,2,200,31])
    print (longest_path(G))
