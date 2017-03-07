import glob, os, re

print (os.getcwd())
currentDir = os.getcwd()

class tile():

	def __init__(self, name):
		self.filename =		name
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

def check_exception():
	pass

def try_print():
	

def loop_files():
	counter = 0
	exceptions = []

	for subdir, dirs, files in os.walk(currentDir):
		#for file in files:
		#	print (os.path.join(subdir, file))
		if counter < 100:
			for file in files:
				if not ".meta" in file and not ".py" in file and not "_" in file[:1]:
					counter += 1
					stripped = re.findall("(?:.*?_){2}(.*)", file) #Matches everything after the second underscore
					print ((re.search("(?<=_)(.*?)(?=_)", file)).group(0))
					print ((re.search("[^_]*", file)).group(0))
					tilejob = tile(stripped)
					print (file)
					#print (subdir)
					#print (stripped)
			#for directory in dirs:
			#	print (directory)

	print (counter)


	def test2():

		for subdir, dirs, files in os.walk(currentDir):
				for file in files:
					if not ".meta" in file and not ".py" in file and not "_" in file[:1]:

						stripped = re.findall("(?:.*?_){2}(.*)", file) 
						print (file)
						print (subdir)

		print (counter)


loop_files()