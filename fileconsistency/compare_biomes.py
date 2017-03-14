import glob, os, re, csv, sys

print (os.getcwd())
currentDir = os.getcwd()

class tile():

	def __init__(self, name):
		self.filename =		name
		self.fileLoc =		""
		self.fr =			False
		self.mn =			False
		self.hl =			False
		self.st =			False
		self.sw = 			False
		self.frStyle =		""
		self.mnStyle =		""
		self.hlStyle =		""
		self.stStyle =		""
		self.swStyle =		""

	def check_consistency(self):
		fileLoc = str(os.getcwd() + "test")

	def remove_biome(self):
		print ("test")

def get_files():
	for file in glob.glob("*.*"):
		if "_OUT" in file and not "PSG" in file:
			if not ".meta" in file: 
			#file = file[:-34]
				print (file)

def loop_files():
	counter = 0
	exceptions = []

	for subdir, dirs, files in os.walk(currentDir):
		#for file in files:
		#	print (os.path.join(subdir, file))
		#if counter < 4000:
			for file in files:
				fileBiome = ((re.search("[^_]*", file)))
				fileLevel = ((re.search("(?<=_)(.*?)(?=_)", file)))
				if  fileBiome.group(0).upper() == "FOREST" or fileBiome.group(0).upper() == "STEPPE" or fileBiome.group(0).upper() == "MOUNTAIN" or fileBiome.group(0).upper() == "HIGHLAND" or fileBiome.group(0).upper() == "SWAMP":
					if  fileLevel.group(0).upper() == "GREEN" or fileLevel.group(0).upper() == "RED" or fileLevel.group(0).upper() == "DEAD":
						if not ".meta" in file and not ".py" in file and not "_" in file[:1]:
							counter += 1
							stripped = re.findall("(?:.*?_){2}(.*)", file) #Matches everything after the second underscore
							#stripped = stripped[0]
							#if fileBiome:
							#	print (fileBiome.group(0))
							#if fileLevel:
							#	print (fileLevel.group(0))
							#print ((re.search("(?<=_)(.*?)(?=_)", file)).group(0))
							#tilejob = tile(stripped)
							#print (file)
							#print (stripped[0])
							#print (search_list(stripped))
							search_list(stripped, subdir, fileBiome.group(0), fileLevel.group(0))
							#print (counter)
							

							#print (subdir)
							#print (stripped)
			#for directory in dirs:
			#	print (directory)

	print (counter)

def search_list(item, location, biome, style):
	#found = False
	for entry in prefabList:
		#print (entry['prefab'])
		#print (item)
		#print ("\n")
		if item == entry['prefab']:
			#print (entry['prefab'])
			#print (item)
			add_biome_style(item, location, biome, style)
			return
	add_list(item, location, biome, style)
	return
	#return False

def add_list(item, location, biome, style):
	item_dict = {'prefab': "", 'location': [], 'SW': False, 'ST': False, 'MN': False, 'HL': False, 'FR': False, 'SWStyle': [], 'STStyle': [], 'MNStyle': [], 'HLStyle': [], 'FRStyle': []}
	#item_dict = {'prefab': "", 'location': [], 'biome': [], 'style': []}

	item_dict['prefab'] = item
	item_dict['location'].append(location)

	item_dict[return_biome_abr(biome)] = True

	item_dict[(return_biome_abr(biome)+'Style')].append(style)





	prefabList.append(item_dict)

def return_biome_abr(biome):
	if biome.upper() == "SWAMP":
		return "SW"
	if biome.upper() == "STEPPE":
		return "ST"
	if biome.upper() == "MOUNTAIN":
		return "MN"
	if biome.upper() == "HIGHLAND":
		return "HL"
	if biome.upper() == "FOREST":
		return "FR"
	else:
		input('Press enter to continue: ')

def add_biome_style(item, location, biome, style):
	if style.upper() == "GREEN":
		style = "G"
	elif style.upper() == "RED":
		style = "R"
	elif style.upper() == "DEAD":
		style = "D"
	else:
		style = "No style?"

	for eachEntry in prefabList:
		#print (eachEntry['prefab'])
		#print (item)
		#print ("\n")
		if item == eachEntry['prefab']:
			eachEntry['location'].append(location) 
			eachEntry[return_biome_abr(biome)] = True
			eachEntry[(return_biome_abr(biome)+'Style')].append(style)

			#eachEntry['biome'].append(biome) 
			#eachEntry['style'].append(style) 

def print_data():
	for each in prefabList:
		for entry in each['prefab']:
			print (entry)
		for entry in each['location']:
			print (entry)
		for entry in each['biome']:
			print (entry)
		for entry in each['style']:
			print (entry)

		print ("\n")

def print_data2():
	printStyle = "";
	appendLine = ""
	for each in prefabList:
		for entry in each['prefab']:
			appendLine += entry
			print (entry)

		if not each['SW'] == False:
			print ("SW: ", each['SW'])
			appendLine += ", SWAMP"
		else:
			appendLine += ","
		#print (each['SWStyle'])
		for style in each['SWStyle']:
			printStyle += (style + " ")
		if not printStyle == "":
			print (printStyle[:-1])
			appendLine += ", "
			appendLine += printStyle
		else:
			appendLine += (",")
		printStyle = ""


		if not each['ST'] == False:
			print ("ST: ", each['ST'])
			appendLine += ", STEPPE"
		else:
			appendLine += ","
		#print (each['STStyle'])
		for style in each['STStyle']:
			printStyle += (style + " ")
		if not printStyle == "":
			print (printStyle[:-1])
			appendLine += ", "
			appendLine += printStyle
		else:
			appendLine += (",")
		printStyle = ""


		if not each['MN'] == False:
			print ("MN: ", each['MN'])
			appendLine += ", MOUNTAIN"
		else:
			appendLine += ","
		#print (each['MNStyle'])
		for style in each['MNStyle']:
			printStyle += (style + " ")
		if not printStyle == "":
			print (printStyle[:-1])
			appendLine += ", "
			appendLine += printStyle
		else:
			appendLine += (",")
		printStyle = ""


		if not each['HL'] == False:
			print ("HL: ", each['HL'])
			appendLine += ", HIGHLAND"
		else:
			appendLine += ","
		#print (each['HLStyle'])
		for style in each['HLStyle']:
			printStyle += (style + " ")
		if not printStyle == "":
			print (printStyle[:-1])
			appendLine += ", "
			appendLine += printStyle
		else:
			appendLine += (",")
		printStyle = ""


		if not each['FR'] == False:
			print ("FR: ", each['FR'])
			appendLine += ", FOREST"
		else:
			appendLine += ","
		#print (each['FRStyle'])
		for style in each['FRStyle']:
			printStyle += (style + " ")
		if not printStyle == "":
			print (printStyle[:-1])
			appendLine += ", "
			appendLine += printStyle
		else:
			appendLine += (",")
		printStyle = ""


		for entry in each['location']:
			print (entry)



		print ("\n")

		writeList.append(appendLine)
		appendLine = ""

writeList = []
prefabList = []
loop_files()
print ("\n\n\n\n")
#print_data()
print_data2()



d = open()
f = open("output.csv", "wt", newline='', quoting=csv.QUOTE_NONE)
try:
	writer = csv.writer(f)
	for entry in writeList:
		writer.writerow([entry])
finally: 
	f.close()