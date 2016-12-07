import networkx as nx
from natsort import natsorted
import itertools
import matplotlib.pyplot as plot
import random
import re

##################################
#          DATA SECTION
#      FROM THE GOOGLE SHEET
##################################




edge_list = ["N C_01", "route_01", "E C_01", "route_02", "S C_01", "route_03", "W C_01", "route_04"]
nodes = ['N', 'E', 'S', 'W', 'C_01']
edges = [('N', 'C_01'), ('E', 'C_01'), ('S', 'C_01'), ('W', 'C_01')]
route_list = ['route_01', 'route_02', 'route_03', 'route_04']
list_of_crossings = ['crossing_01']
crossing_01 = ['route', 'C_01', 'route_01', 'route_02', 'route_03', 'route_04']








##################################
#        END OF SHEET DATA
##################################

def init(node_list, list_of_edges):
    nodes = node_list

    edges = list_of_edges

    G=nx.Graph()

    for n in nodes:
        G.add_node(n)

    for e in edges:
        G.add_edge(e[0], e[1])

    return (G, edges)

def find_crossing(roadtype, slot, N_con=False, E_con=False, S_con=False, W_con=False):
    biome = "HL"
    if   N_con == True      and E_con == False      and S_con ==False       and W_con == False:
        return ("[|_StreetCrossing", slot, "0", "[" + roadtype + "_D_01]", "true]")
        #return (roadtype + "_D"), "0"
    elif N_con == True      and E_con == False      and S_con == True       and W_con == False:
        rotations = ["0", "180"]
        return ("[|_StreetCrossing", slot, random.choice(rotations), "[" + roadtype + "_I_01]", "true]")
        #return (roadtype + "_I"), random.choice(rotations)
    elif N_con == True      and E_con == True       and S_con == False      and W_con == False:
        return ("[|_StreetCrossing", slot, "0", "[" + roadtype + "_L_01]", "true]")
        #return (roadtype + "_L"), "0"
    elif N_con == True      and E_con == True       and S_con == True       and W_con == False:
        return ("[|_StreetCrossing", slot, "0", "[" + roadtype + "_T_01]", "true]")
        #return (roadtype + "_T"), "0"
    elif N_con == True      and E_con == True       and S_con == True       and W_con == True:
        rotations = ["0", "90", "180", "270"]
        return ("[|_StreetCrossing", slot, random.choice(rotations), "[" + roadtype + "_X_01]", "true]")
        #return (roadtype + "_X"), random.choice(rotations)
    elif N_con == True      and E_con == False      and S_con == True       and W_con == True:
        return ("[|_StreetCrossing", slot, "180", "[" + roadtype + "_T_01]", "true]")
        #return (roadtype + "_T"), "180"
    elif N_con == True      and E_con == False      and S_con == False      and W_con == True:
        return ("[|_StreetCrossing", slot, "270", "[" + roadtype + "_L_01]", "true]")
        #return (roadtype + "_L"), "270"
    elif N_con == True      and E_con == True       and S_con == False      and W_con == True:
        return ("[|_StreetCrossing", slot, "270", "[" + roadtype + "_T_01]", "true]")
        #return (roadtype + "_T"), "270"

    elif N_con == False     and E_con == True       and S_con == False      and W_con == False:
        return ("[|_StreetCrossing", slot, "90", "[" + roadtype + "_D_01]", "true]")
        #return (roadtype + "_D"), "90"
    elif N_con == False     and E_con == True       and S_con == False      and W_con == True:
        rotations = ["90", "270"]
        return ("[|_StreetCrossing", slot, random.choice(rotations), "[" + roadtype + "_I_01]", "true]")
        #return (roadtype + "_I"), random.choice(rotations)
    elif N_con == False     and E_con == True       and S_con == True       and W_con == False:
        return ("[|_StreetCrossing", slot, "90", "[" + roadtype + "_L_01]", "true]")
        #return (roadtype + "_L"), "90"
    elif N_con == False     and E_con == True       and S_con == True       and W_con == True:
        return ("[|_StreetCrossing", slot, "90", "[" + roadtype + "_T_01]", "true]")
        #return (roadtype + "_T"), "90"

    elif N_con == False     and E_con == False      and S_con == True       and W_con == False:
        return ("[|_StreetCrossing", slot, "180", "[" + roadtype + "_D_01]", "true]")
        #return (roadtype + "_D"), "180"
    elif N_con == False     and E_con == False      and S_con == True       and W_con == True:
        return ("[|_StreetCrossing", slot, "180", "[" + roadtype + "_L_01]", "true]")
        #return (roadtype + "_L"), "180"
    elif N_con == False     and E_con == False      and S_con == False      and W_con == True:
        return ("[|_StreetCrossing", slot, "270", "[" + roadtype + "_D_01]", "true]")
        #return (roadtype + "_D"), "270"

    else:
        return ("[|_StreetCrossing", slot, "0", "[NONE]", "true]")
        #return (roadtype + "_none")

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
    #print (point_a + point_b + ":\n" + str(test_len), "\n")
    test_len.sort(key=len)
    if len(test_len) > 1:
        test_len = test_len[0]
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
    #print (r2, "\n")
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

    val_map = {'N': 1.5,
               'E': 1.5,
               'S': 1.5,
               'W': 1.5
               }

    #values = [val_map.get(node, 1) for node in G.nodes()]

    pos = nx.spectral_layout(G, dim=2, scale=50)

    #nx.draw_networkx_nodes(G, pos, node_color=values)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels)

    plot.axis("off")
    plot.show()

def paths(): #probably something is fucked in here

    pathNE = two_points("N", "E")
    pathNS = two_points("N", "S")
    pathNW = two_points("N", "W")
    pathES = two_points("E", "S")
    pathEW = two_points("E", "W")
    pathSW = two_points("S", "W")

    #print ("NES: ")
    pathNES = add_point(pathNE, "S")
    pathNES = path_sort(pathNES)
    #print ("ESW: ")
    pathESW = add_point(pathES, "W")
    pathESW = path_sort(pathESW)
    #print ("SWN: ")
    pathSWN = add_point(pathSW, "N")
    pathSWN = path_sort(pathSWN)
    #print ("NEW: ")
    pathNEW = add_point(pathNE, "W")
    pathNEW = path_sort(pathNEW)
    #print ("NESW:")
    pathNESW = add_point(pathNES, "W")
    pathNESW = path_sort(pathNESW)

    #pathNc1 = two_points("N", "c1", 0)
    #pathEc1 = two_points("E", "c1", 0)
    #PathSc2 = two_points("S", "c2", 0)
    #PathWc2 = two_points("W", "c2", 0)

    pathNc1 = two_points(edges[0][0], edges[0][1], 0)
    pathEc1 = two_points(edges[1][0], edges[1][1], 0)
    pathSc2 = two_points(edges[2][0], edges[2][1], 0)
    pathWc2 = two_points(edges[3][0], edges[3][1], 0)


    pathNE = rem_bracket(pathNE)
    #if len(pathNS) > 1:
    #    pathNS = pathNS[0]
    pathNS = rem_bracket(pathNS)
    pathNW = rem_bracket(pathNW)
    pathES = rem_bracket(pathES)
    pathEW = rem_bracket(pathEW)
    pathSW = rem_bracket(pathSW)
    pathNES = rem_bracket(pathNE)
    pathESW = rem_bracket(pathESW)
    pathSWN = rem_bracket(pathSWN)
    pathNEW = rem_bracket(pathNEW)
    pathNESW = rem_bracket(pathNESW)
    pathNc1 = rem_bracket(pathNc1)
    pathEc1 = rem_bracket(pathEc1)
    pathSc2 = rem_bracket(pathSc2)
    pathWc2 = rem_bracket(pathWc2)

    all_lists = []
    all_lists.append(pathNE)
    all_lists.append(pathNS)
    all_lists.append(pathNW)
    all_lists.append(pathES)
    all_lists.append(pathEW)
    all_lists.append(pathSW)
    all_lists.append(pathNES)
    all_lists.append(pathESW)
    all_lists.append(pathSWN)
    all_lists.append(pathNEW)
    all_lists.append(pathNESW)
    all_lists.append(pathNc1)
    all_lists.append(pathEc1)
    all_lists.append(pathSc2)
    all_lists.append(pathWc2)

    #print (pathNE)



    return all_lists

def rem_bracket(double_bracket):
    new_list = []
    #print (type(double_bracket))
    if len(double_bracket) > 1 and not isinstance(double_bracket[0],str):
        #print (isinstance(double_bracket[0],str))
        new_list = double_bracket[0]
        #print ("list has more than one element")
        return new_list #wrong
    elif isinstance(double_bracket[0],str):
        return double_bracket
    else:
        for n in double_bracket:
            new_list = n
        return new_list

def find_route(list_of_lists, list_of_edges):
    output = []
    for n in list_of_lists:
        if len(n)>1:
            #print (n[0], n[1])
            combine = n[0] + " " + n[1]
            for i in [i for i,x in enumerate(list_of_edges) if x == combine]:
                output.append(list_of_edges[(i+1)])
        else:
            output.append(list_of_edges[1])
    
    set2 = set(output)
    result = list(set2)
    return result

def get_index(list_to_check, search):
    index = list_to_check.index(search)
    return index

def get_crossing(crossing, print_list):
    crossing_result = [crossing[0], crossing[1] ,False, False, False, False]
    index = ""
    for c in crossing[2:]:
        if (c + "_on") in print_list:
            index = get_index(crossing, c)
            crossing_result[index] = True
    crossing = find_crossing(crossing_result[0], crossing_result[1], crossing_result[2], crossing_result[3], crossing_result[4], crossing_result[5])
    return crossing

def main_func():
    loop_count = 0
    for n, x in itertools.zip_longest(all_lists, path_names):
        loop_count += 1
        print_list = ""
        #crossing_result = [crossing_01[0], False, False, False, False]
        index = ""
        crossings = []


        list_of_tuples = list(itertools.permutations(n))
        list_of_lists = [list(elem) for elem in list_of_tuples]
        routes = find_route(list_of_lists, edge_list)
        routes = sorted(routes)
        for i in routes:
            if 'NONE' in i:
                continue
            print_list += "'" + i + "_on'" + ", "
        #print_list = print_list[:-2]
        for r in route_list:
            if not r in print_list and not 'NONE' in r:
                print_list += "'" + r + "_off'" + ", "
        print_list = print_list[:-2]
        #for c in list_of_crossings:
        #    crossings.append(get_crossing(eval(c), print_list))
        #for c in crossing_01[1:]:
        #    if (c + "_on") in print_list:
        #        index = get_index(crossing_01, c)
        #        crossing_result[index] = True
        #crossing = find_crossing(crossing_result[0], crossing_result[1], crossing_result[2], crossing_result[3], crossing_result[4])
        #print (x + "\n" + print_list + ", " + str(crossings) + "\n\n")
        cross = []
        s = ""
        for c in list_of_crossings:
            cross.append(get_crossing(eval(c), print_list))
        #s += (cross[0] + cross[1])

        s += "(" + ', '.join(map(str,cross)) + ")"
        s = re.sub('[(){}<>]', '', s)
        teststring = (x + "\t=counta(indirect(ADDRESS(row()+1,COLUMN()-1)):indirect(address(row()+3,column()-1)))\n" + print_list + ", \t" + s + "\n\n")
        teststring = re.sub("\'\[", "['", teststring)
        teststring = re.sub("\]\'", "']", teststring)
        print (teststring)
    if loop_count == 15:
        print (str(loop_count) + " paths found. This is valid data.")
    else:
        print ("ERROR")

G, edges = init(nodes, edges)

all_lists = paths()

#draw_graph()

path_names = ["NE", "NS", "NW", "ES", "EW", "SW", "NES", "ESW", "NSW", "NEW", "NESW", "N", "E", "S", "W"]

main_func()