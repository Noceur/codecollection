

#dict test keys by permutations
edge_list = ["N c1", "route 1", "E c1", "route 2", "S c2", "route 3", "W c2", "route 4", "c1 c2", "route 5"]
list_of_tuples = [('E', 'N', 'S', 'c1', 'c2'), ('E', 'N', 'S', 'c2', 'c1'), ('E', 'N', 'c1', 'S', 'c2'), ('E', 'N', 'c1', 'c2', 'S'), ('E', 'N', 'c2', 'S', 'c1'), ('E', 'N', 'c2', 'c1', 'S'), ('E', 'S', 'N', 'c1', 'c2'), ('E', 'S', 'N', 'c2', 'c1'), ('E', 'S', 'c1', 'N', 'c2'), ('E', 'S', 'c1', 'c2', 'N'), ('E', 'S', 'c2', 'N', 'c1'), ('E', 'S', 'c2', 'c1', 'N'), ('E', 'c1', 'N', 'S', 'c2'), ('E', 'c1', 'N', 'c2', 'S'), ('E', 'c1', 'S', 'N', 'c2'), ('E', 'c1', 'S', 'c2', 'N'), ('E', 'c1', 'c2', 'N', 'S'), ('E', 'c1', 'c2', 'S', 'N'), ('E', 'c2', 'N', 'S', 'c1'), ('E', 'c2', 'N', 'c1', 'S'), ('E', 'c2', 'S', 'N', 'c1'), ('E', 'c2', 'S', 'c1', 'N'), ('E', 'c2', 'c1', 'N', 'S'), ('E', 'c2', 'c1', 'S', 'N'), ('N', 'E', 'S', 'c1', 'c2'), ('N', 'E', 'S', 'c2', 'c1'), ('N', 'E', 'c1', 'S', 'c2'), ('N', 'E', 'c1', 'c2', 'S'), ('N', 'E', 'c2', 'S', 'c1'), ('N', 'E', 'c2', 'c1', 'S'), ('N', 'S', 'E', 'c1', 'c2'), ('N', 'S', 'E', 'c2', 'c1'), ('N', 'S', 'c1', 'E', 'c2'), ('N', 'S', 'c1', 'c2', 'E'), ('N', 'S', 'c2', 'E', 'c1'), ('N', 'S', 'c2', 'c1', 'E'), ('N', 'c1', 'E', 'S', 'c2'), ('N', 'c1', 'E', 'c2', 'S'), ('N', 'c1', 'S', 'E', 'c2'), ('N', 'c1', 'S', 'c2', 'E'), ('N', 'c1', 'c2', 'E', 'S'), ('N', 'c1', 'c2', 'S', 'E'), ('N', 'c2', 'E', 'S', 'c1'), ('N', 'c2', 'E', 'c1', 'S'), ('N', 'c2', 'S', 'E', 'c1'), ('N', 'c2', 'S', 'c1', 'E'), ('N', 'c2', 'c1', 'E', 'S'), ('N', 'c2', 'c1', 'S', 'E'), ('S', 'E', 'N', 'c1', 'c2'), ('S', 'E', 'N', 'c2', 'c1'), ('S', 'E', 'c1', 'N', 'c2'), ('S', 'E', 'c1', 'c2', 'N'), ('S', 'E', 'c2', 'N', 'c1'), ('S', 'E', 'c2', 'c1', 'N'), ('S', 'N', 'E', 'c1', 'c2'), ('S', 'N', 'E', 'c2', 'c1'), ('S', 'N', 'c1', 'E', 'c2'), ('S', 'N', 'c1', 'c2', 'E'), ('S', 'N', 'c2', 'E', 'c1'), ('S', 'N', 'c2', 'c1', 'E'), ('S', 'c1', 'E', 'N', 'c2'), ('S', 'c1', 'E', 'c2', 'N'), ('S', 'c1', 'N', 'E', 'c2'), ('S', 'c1', 'N', 'c2', 'E'), ('S', 'c1', 'c2', 'E', 'N'), ('S', 'c1', 'c2', 'N', 'E'), ('S', 'c2', 'E', 'N', 'c1'), ('S', 'c2', 'E', 'c1', 'N'), ('S', 'c2', 'N', 'E', 'c1'), ('S', 'c2', 'N', 'c1', 'E'), ('S', 'c2', 'c1', 'E', 'N'), ('S', 'c2', 'c1', 'N', 'E'), ('c1', 'E', 'N', 'S', 'c2'), ('c1', 'E', 'N', 'c2', 'S'), ('c1', 'E', 'S', 'N', 'c2'), ('c1', 'E', 'S', 'c2', 'N'), ('c1', 'E', 'c2', 'N', 'S'), ('c1', 'E', 'c2', 'S', 'N'), ('c1', 'N', 'E', 'S', 'c2'), ('c1', 'N', 'E', 'c2', 'S'), ('c1', 'N', 'S', 'E', 'c2'), ('c1', 'N', 'S', 'c2', 'E'), ('c1', 'N', 'c2', 'E', 'S'), ('c1', 'N', 'c2', 'S', 'E'), ('c1', 'S', 'E', 'N', 'c2'), ('c1', 'S', 'E', 'c2', 'N'), ('c1', 'S', 'N', 'E', 'c2'), ('c1', 'S', 'N', 'c2', 'E'), ('c1', 'S', 'c2', 'E', 'N'), ('c1', 'S', 'c2', 'N', 'E'), ('c1', 'c2', 'E', 'N', 'S'), ('c1', 'c2', 'E', 'S', 'N'), ('c1', 'c2', 'N', 'E', 'S'), ('c1', 'c2', 'N', 'S', 'E'), ('c1', 'c2', 'S', 'E', 'N'), ('c1', 'c2', 'S', 'N', 'E'), ('c2', 'E', 'N', 'S', 'c1'), ('c2', 'E', 'N', 'c1', 'S'), ('c2', 'E', 'S', 'N', 'c1'), ('c2', 'E', 'S', 'c1', 'N'), ('c2', 'E', 'c1', 'N', 'S'), ('c2', 'E', 'c1', 'S', 'N'), ('c2', 'N', 'E', 'S', 'c1'), ('c2', 'N', 'E', 'c1', 'S'), ('c2', 'N', 'S', 'E', 'c1'), ('c2', 'N', 'S', 'c1', 'E'), ('c2', 'N', 'c1', 'E', 'S'), ('c2', 'N', 'c1', 'S', 'E'), ('c2', 'S', 'E', 'N', 'c1'), ('c2', 'S', 'E', 'c1', 'N'), ('c2', 'S', 'N', 'E', 'c1'), ('c2', 'S', 'N', 'c1', 'E'), ('c2', 'S', 'c1', 'E', 'N'), ('c2', 'S', 'c1', 'N', 'E'), ('c2', 'c1', 'E', 'N', 'S'), ('c2', 'c1', 'E', 'S', 'N'), ('c2', 'c1', 'N', 'E', 'S'), ('c2', 'c1', 'N', 'S', 'E'), ('c2', 'c1', 'S', 'E', 'N'), ('c2', 'c1', 'S', 'N', 'E')]

list_of_lists = [list(elem) for elem in list_of_tuples]

edgeLabels = {
    ("N","c1"):"route 1",
    ("E","c1"):"route 2",
    ("S","c2"):"route 3",
    ("W","c2"):"route 4",
    ("c1","c2"):"route 5"
}

def find_route(list_of_lists, edge_List):
	output = []
	for n in list_of_lists:
		llistlen = len(n)
		combine = n[0] + " " + n[1]
		for i in [i for i,x in enumerate(edge_list) if x == combine]:
			#print (i)
			output.append(edge_list[(i+1)])
		combine = n[0] + " " + n[1]
		for i in [i for i,x in enumerate(edge_list) if x == combine]:
			#print (i)
			output.append(edge_list[(i+1)])
	
	set2 = set(output)
	result = list(set2)
	return result


test = []
test = find_route(list_of_lists, edge_list)
for l in test:
	print (l)