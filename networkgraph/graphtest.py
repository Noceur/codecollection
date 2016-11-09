import networkx as nx
from natsort import natsorted
import itertools
import matplotlib.pyplot as plot

def init():
    nodes = ["N", "E", "S", "W", "c1", "c2"]

    edges = [
    ("N", "c1"),
    ("E", "c1"),
    ("S", "c2"),
    ("W", "c2"),
    ("c1", "c2")
    ]

    G=nx.Graph()

    for n in nodes:
    	G.add_node(n)

    for e in edges:
    	G.add_edge(e[0], e[1])

    return G

def find_all_paths_lim(graph, start, end, k, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            if len(path) < k+1:
                newpaths = find_all_paths_lim(graph, node, end, k, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

def two_points(point_a, point_b, max_solutions=0):
    i=0
    test_len = []
    while not len(test_len)>max_solutions:
        i += 1
        test_len = find_all_paths_lim(G, point_a, point_b, i)
    print (point_a + point_b + ":", test_len, "\n\n")
    test_len.sort(key=len)
    return test_len

def add_point(path, point_c):
    r = []
    for n in path:
        i=0
        for n2 in n:
            i+=1
            t = find_all_paths_lim(G, n2, point_c, i)
            for n3 in t:
                merge = n + n3
                r.append(merge)
                merge = []
    r = [x for x in r if x != []]
    r.sort(key=len)
    return r

def f7(seq): #gets rid of duped lists.
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def path_sort(path_to_sort):
    r2 = []
    for n in path_to_sort:
        n = natsorted(n)
        r2.append(f7(n))

    r2.sort(key=len)
    r2 = list(r2 for r2,_ in itertools.groupby(r2))
    print (r2, "\n")
    #print (len(r2))
    return r2

def draw_graph():
    #edgeLabels = {edges: x for x, edges in enumerate(edges)}
    edgeLabels = {
        ("N","c1"):'route 1',
        ("E","c1"):'route 2',
        ("S","c2"):'route 3',
        ("W","c2"):'route 4',
        ("c1","c2"):'route 5'
    }

    val_map = {'N': 0.5,
               'E': 0.5,
               'S': 0.5,
               'W': 0.5
               }

    values = [val_map.get(node, 0.25) for node in G.nodes()]

    pos = nx.spectral_layout(G, dim=2, scale=50)

    nx.draw_networkx_nodes(G, pos, node_color=values)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels)

    plot.axis("off")
    plot.show()

def paths():
    pathNE = two_points("N", "E")
    pathNS = two_points("N", "S")
    pathNW = two_points("N", "W")
    pathES = two_points("E", "S")
    pathEW = two_points("E", "W")
    pathSW = two_points("S", "W")

    print ("NES: ")
    pathNES = add_point(pathNE, "S")
    path_sort(pathNES)
    print ("ESW: ")
    pathESW = add_point(pathES, "W")
    path_sort(pathESW)
    print ("SWN: ")
    pathSWN = add_point(pathSW, "N")
    path_sort(pathSWN)
    print ("NEW: ")
    pathNEW = add_point(pathNE, "W")
    path_sort(pathNEW)
    print ("NESW:")
    pathNESW = add_point(pathNES, "W")
    path_sort(pathNESW)

    pathNc1 = two_points("N", "c1", 0)
    pathEc2 = two_points("E", "c1", 0)
    PathSc3 = two_points("S", "c2", 0)
    PathWc4 = two_points("W", "c2", 0)


G = init()

paths()

draw_graph()