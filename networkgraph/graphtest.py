import networkx as nx
from natsort import natsorted
import itertools

'''G=nx.Graph()
G.add_edge("A", "1")
G.add_edge("B", "2")
G.add_edge("C", "3")
G.add_edge("D", "4")
G.add_edge("1", "5")
G.add_edge("1", "10")
G.add_edge("2", "6")
G.add_edge("2", "7")
G.add_edge("3", "7")
G.add_edge("3", "8")
G.add_edge("4", "9")
G.add_edge("4", "10")
G.add_edge("5", "11")
G.add_edge("5", "10")
G.add_edge("5", "6")
G.add_edge("6", "7")
G.add_edge("6", "11")
G.add_edge("7", "8")
G.add_edge("8", "9")
G.add_edge("8", "11")
G.add_edge("8", "3")
G.add_edge("9", "4")
G.add_edge("9", "11")
G.add_edge("11", "8")'''

G=nx.Graph()
G.add_edge("A", "1")
G.add_edge("B", "2")
G.add_edge("C", "3")
G.add_edge("D", "4")
G.add_edge("1", "5")
G.add_edge("1", "6")
G.add_edge("2", "6")
G.add_edge("2", "7")
G.add_edge("3", "7")
G.add_edge("3", "8")
G.add_edge("4", "8")
G.add_edge("4", "5")
G.add_edge("5", "6")
G.add_edge("5", "8")
G.add_edge("6", "7")
G.add_edge("7", "8")

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

def two_points(point_a, point_b, max_solutions=5):
    i=0
    test_len = []
    while not len(test_len)>max_solutions:
        i += 1
        test_len = find_all_paths_lim(G, point_a, point_b, i)
    print (test_len, "\n\n")
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
    #print ("\n\n\n\n\n\n", r2)
    print (len(r2))
    return r2

'''def run_2_points(a, b):
    path = tw

def run_3_points():


def run_4_points():'''




path1 = two_points("A", "C")
#path2 = add_point(path1, "B")
#path3 = add_point(path2, "D")
path_sort(path1)