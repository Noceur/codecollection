import random
import itertools
from collections import Counter
from natsort import natsorted

def find_crossing(roadtype, N_con=False, E_con=False, S_con=False, W_con=False):
	if   N_con == True		and E_con == False		and S_con ==False 		and W_con == False:
		return (roadtype + "_D"), "0"
	elif N_con == True		and E_con == False		and S_con == True		and W_con == False:
		rotations = ["0", "180"]
		return (roadtype + "_I"), random.choice(rotations)
	elif N_con == True		and E_con == True		and S_con == False		and W_con == False:
		return (roadtype + "_L"), "0"
	elif N_con == True		and E_con == True		and S_con == True		and W_con == False:
		return (roadtype + "_T"), "0"
	elif N_con == True		and E_con == True		and S_con == True		and W_con == True:
		rotations = ["0", "90", "180", "270"]
		return (roadtype + "_X"), random.choice(rotations)
	elif N_con == True		and E_con == False		and S_con == True		and W_con == True:
		return (roadtype + "_T"), "180"
	elif N_con == True		and E_con == False		and S_con == False		and W_con == True:
		return (roadtype + "_L"), "270"
	elif N_con == True		and E_con == True		and S_con == False		and W_con == True:
		return (roadtype + "_T"), "270"

	elif N_con == False		and E_con == True		and S_con == False		and W_con == False:
		return (roadtype + "_D"), "90"
	elif N_con == False		and E_con == True		and S_con == False		and W_con == True:
		rotations = ["90", "270"]
		return (roadtype + "_I"), random.choice(rotations)
	elif N_con == False		and E_con == True		and S_con == True		and W_con == False:
		return (roadtype + "_L"), "90"
	elif N_con == False		and E_con == True		and S_con == True		and W_con == True:
		return (roadtype + "_T"), "90"

	elif N_con == False		and E_con == False		and S_con == True		and W_con == False:
		return (roadtype + "_D"), "180"
	elif N_con == False		and E_con == False		and S_con == True		and W_con == True:
		return (roadtype + "_L"), "180"
	elif N_con == False		and E_con == False		and S_con == False		and W_con == True:
		return (roadtype + "_D"), "270"

	else:
		return (roadtype + "_none")

edgeLabels = {
    ("N","c1"):'route 1',
    ("E","c1"):'route 2',
    ("S","c2"):'route 3',
    ("W","c2"):'route 4',
    ("c1","c2"):'route 5'
}

test_list = ['N', 'E', 'S', 'W', 'c1', 'c2']
output = list(itertools.permutations(test_list, 2))

def f7(seq): #gets rid of duped lists.
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

output = f7(output)

def selectUnique(x):
    count = Counter((i[1], i[2]) for i in x)
    out = [i for i in x if count[(i[1], i[2])] == 1]
    return out

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

#output = selectUnique(output)

#print (output)

#for n in output:
#	print (n)

output2 = []

for n in output:
	output2.append(sorted(n))

output2 = [list(elem) for elem in output2]


output2 = path_sort(output2)
#output2 = f7(output2)



print (len(output2))
print (output2)