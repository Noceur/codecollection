import glob, os, re, csv, sys

print (os.getcwd())
currentDir = os.getcwd()

def loop_files():
	counter = 0
	exceptions = []
	#currentDir = ""
	for subdir, dirs, files in os.walk(currentDir):
		#for file in files:
		#	print (os.path.join(subdir, file))
		#if counter < 8000:
			for file in files:
				fileBiome = ((re.search("[^_]*", file)))
				fileLevel = ((re.search("(?<=_)(.*?)(?=_)", file)))
				if  fileBiome.group(0).upper() == "FOREST" or fileBiome.group(0).upper() == "STEPPE" or fileBiome.group(0).upper() == "MOUNTAIN" or fileBiome.group(0).upper() == "HIGHLAND" or fileBiome.group(0).upper() == "SWAMP":
					if  fileLevel.group(0).upper() == "GREEN" or fileLevel.group(0).upper() == "RED" or fileLevel.group(0).upper() == "DEAD":
						if not ".meta" in file and not ".py" in file and not "_" in file[:1]:
							#print (file[:-7])
							dirCurrent = subdir.split(os.path.sep)[-1] #Get current directory
							#print (subdir.split(os.path.sep)[-1])
							counter += 1
							stripped = re.findall("(?:.*?_){2}(.*)", file) #Matches everything after the second underscore
							stripped = (stripped[0][:-7])
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
							search_list(stripped, subdir, fileBiome.group(0), fileLevel.group(0), dirCurrent)
							#print (counter)
							

							#print (subdir)
							#print (stripped)
			#for directory in dirs:
			#	print (directory)

	print (counter)

def search_list(item, location, biome, style, dirCurrent):
	#found = False
	for entry in prefabList:
		#print (entry['prefab'])
		#print (item)
		#print ("\n")
		if item == entry['prefab']:
			#print (entry['prefab'])
			#print (item)
			add_biome_style(item, location, biome, style, dirCurrent)
			return
	add_list(item, location, biome, style, dirCurrent)
	return
	#return False

def add_list(item, location, biome, style, dirCurrent):
	item_dict = {'prefab': "", 'dirCurrent': "", 'location': [], 'SW': False, 'ST': False, 'MN': False, 'HL': False, 'FR': False, 'SWStyle': [], 'STStyle': [], 'MNStyle': [], 'HLStyle': [], 'FRStyle': [], 'locConsistency': True}

	style = style_abr(style)

	# remove biome and level (red, dead, green) from dirCurrent
	dirCurrent = strip_dirCurrent(dirCurrent)



	item_dict['prefab'] = item
	item_dict['location'].append(location)
	item_dict['dirCurrent'] = dirCurrent
	item_dict[biome_abr(biome)] = True
	item_dict[(biome_abr(biome)+'Style')].append(style)

	prefabList.append(item_dict)

def style_abr(style):
	if style.upper() == "GREEN":
		style = "G"
	elif style.upper() == "RED":
		style = "R"
	elif style.upper() == "DEAD":
		style = "D"
	else:
		style = "No style?"
	return style

def strip_dirCurrent(dirCurrent):
	#print (dirCurrent)
	# remove biome and level (red, dead, green) from dirCurrent
	dirBiome = re.search("^.+?_", dirCurrent)
	dirLevel = re.search("(?<=_)(.*?)(?=_)", dirCurrent)
	if dirLevel:
		dirLevel = dirLevel.group(0)
		if dirLevel.lower() == "green" or dirLevel.lower() == "red" or dirLevel.lower() == "dead":
			dirCurrentOld = (dirCurrent + ".")[:-1]
			#print (dirCurrentOld)
			dirCurrent = dirCurrent.replace("GREEN", "", 1)
			if dirCurrentOld == dirCurrent:
				dirCurrent = dirCurrent.replace("RED", "", 1)
			if dirCurrentOld == dirCurrent:
				dirCurrent = dirCurrent.replace("DEAD", "", 1)
	if dirBiome:
		dirBiome = dirBiome.group(0)
		if "swamp" in dirBiome.lower() or "steppe" in dirBiome.lower() or "mountain" in dirBiome.lower() or "highland" in dirBiome.lower() or "forest" in dirBiome.lower():
			dirCurrent = re.sub("^.+?_", "", dirCurrent)
	#print (dirCurrent)
	return dirCurrent

def biome_abr(biome):
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
		print ("Couldn't find biome abr.")
		input('Press enter to continue: ')

def add_biome_style(item, location, biome, style, dirCurrent):
	style = style_abr(style)

	# remove biome and level (red, dead, green) from dirCurrent
	dirCurrent = strip_dirCurrent(dirCurrent)

	for entry in prefabList:
		if item == entry['prefab']:
			if entry['dirCurrent'] != dirCurrent:
				entry['locConsistency'] = False
			entry['location'].append(location) 
			entry[biome_abr(biome)] = True
			entry[(biome_abr(biome)+'Style')].append(style)

def data_formater(entry, biome, printStyle, appendLine, silent=True): #Makes sure the
	biomeAbr = biome_abr(biome)

	if not entry[biomeAbr] == False:
		if not silent:
			print (biomeAbr + ": ", entry[biomeAbr])
		appendLine += ("\t " + biome)
	else:
		appendLine += "\t"
	for style in entry[(biomeAbr + "Style")]:
		printStyle += (style + " ")
	if not printStyle == "":
		if not silent:
			print (printStyle[:-1])
		appendLine += "\t "
		appendLine += printStyle
	else:
		appendLine += ("\t")
	printStyle = ""

	return appendLine

def data_output(silent=True):
	printStyle = "";
	appendLine = ""
	for each in prefabList:
		for entry in each['prefab']:
			appendLine += entry
			if not silent:
				print (entry)
		appendLine += ("\t"+each['dirCurrent'])

		appendLine = data_formater(each, "SWAMP", printStyle, appendLine, silent)
		appendLine = data_formater(each, "STEPPE", printStyle, appendLine, silent)
		appendLine = data_formater(each, "MOUNTAIN", printStyle, appendLine, silent)
		appendLine = data_formater(each, "HIGHLAND", printStyle, appendLine, silent)
		appendLine = data_formater(each, "FOREST", printStyle, appendLine, silent)

		if not each['locConsistency']:
			appendLine += "\t"
			appendLocation = "=concatenate("
			for i, entry in enumerate(each['location']):

				appendLocation += ('"' + entry + '"')
				if not (i+1) >= len(each['location']):
					appendLocation += (", CHAR(10), ")
				#print (len(each['location']))
				#print (i)
				#appendLocation += entry
			appendLocation += ")"
			appendLocation = appendLocation.replace("\\", "/")
			#print (appendLocation)
			appendLine += appendLocation

		if not silent:
			for entry in each['location']:
				print (entry)
			print ("\n")

		writeList.append(appendLine)
		appendLine = ""

writeList = []
prefabList = []
loop_files()
print ("\n\n\n\n")
#data_output()
data_output(True)



f = open("output.csv", "wt", newline='')
try:
	#writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=',')
	writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='',escapechar='\\')
	#writer = csv.writer(f)
	for entry in writeList:
		writer.writerow([entry])
finally: 
	f.close()