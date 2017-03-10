import glob, os, re

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
		if counter < 10000:
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
	for entry in prefabList:
		print (entry['prefab'])
		print (item)
		#print ("\n")
		if item == entry['prefab']:
			#print ("found")
			add_biome_style(item, location, biome, style)
			return
		else:
			#print ("not found")
			add_list(item, location, biome, style)
			return
	add_list(item, location, biome, style)
	#return False

def add_list(item, location, biome, style):
	'''item_dict = {
		prefab =		item,
		fileLoc = 		location,
		fr =			False,
		mn =			False,
		hl =			False,
		st =			False,
		sw = 			False,
		frStyle =		"",
		mnStyle =		"",
		hlStyle =		"",
		stStyle =		"",
		swStyle =		""
	}'''

	#print (item)

	item_dict = {'prefab': "", 'location': [], 'biome': [], 'style': []}
	item_dict['prefab'] = item
	#item_dict['prefab'].append(item)
	item_dict['location'].append(location)
	item_dict['biome'].append(biome)
	item_dict['style'].append(style)

	#print (item_dict['prefab'])

	prefabList.append(item_dict)

def add_biome_style(item, location, biome, style):
	for eachEntry in prefabList:
		#print (eachEntry['prefab'])
		#print (item)
		#print ("\n")
		if item == eachEntry['prefab']:
			eachEntry['location'].append(location) 
			eachEntry['biome'].append(biome) 
			eachEntry['style'].append(style) 

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

prefabList = []
loop_files()
print ("\n\n\n\n")
#print_data()
