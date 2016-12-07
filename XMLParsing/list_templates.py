import glob, os

def get_files(path):
	L_templates = []
	M_templates = []
	S_templates = []

	os.chdir(path)
	#print (os.getcwd())
	for file in glob.glob("*.unity"):
		file = file[:-6]
		#print (file[0])
		if file[0] == "L":
			L_templates.append(file)
		if file[0] == "M" and file[1] != "N":
			M_templates.append(file)
		if file[0] == "S" and not (file[1] == "W" or file[1] == "T"):
			S_templates.append(file)

	# UNCOMMENT TO SEE TEMPLATES PER BIOME AND SIZE

	#print ("\n\n#######################\n        " + path[:-6] + "\n#######################\n")	
	#for x in L_templates:
	#	print (x)
	#print ("")
	#for x in M_templates:
	#	print (x)
	#print ("")
	#for x in S_templates:
	#	print (x)

	os.chdir(base_path)
	result = []
	result.append(L_templates)
	result.append(M_templates)
	result.append(S_templates)
	return result


all_L = []
all_M = []
all_S = []

base_path = os.getcwd()

all_L.extend(get_files("Swamp\Slave")[0])
all_M.extend(get_files("Swamp\Slave")[1])
all_S.extend(get_files("Swamp\Slave")[2])

all_L.extend(get_files("Steppe\Slave")[0])
all_M.extend(get_files("Steppe\Slave")[1])
all_S.extend(get_files("Steppe\Slave")[2])

all_L.extend(get_files("Forest\Slave")[0])
all_M.extend(get_files("Forest\Slave")[1])
all_S.extend(get_files("Forest\Slave")[2])

all_L.extend(get_files("Highlands\Slave")[0])
all_M.extend(get_files("Highlands\Slave")[1])
all_S.extend(get_files("Highlands\Slave")[2])

all_L.extend(get_files("Mountain\Slave")[0])
all_M.extend(get_files("Mountain\Slave")[1])
all_S.extend(get_files("Mountain\Slave")[2])



print ("L templates")
for each in all_L:
	print (each)

print ("\n\n\nM templates")
for each in all_L:
	print (each)

print ("\n\n\nS templates")
for each in all_S:
	print (each)
