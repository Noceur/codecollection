from xml.etree import ElementTree

#=====================================

tree = ElementTree.parse('world.xml')
root = tree.getroot()
child = root[0]
child2 = root[0][0]

#=====================================

def find_string(searchthrough, tofind): #Takes two strings and tries to find the content of string2 in string1, if it does it prints the index of where it starts.
	try:
		result = searchthrough.find(tofind)
		if result != -1:
			print ("found '" + tofind + "' at index: " + str(result))
	except:
		print ("failed to return")

def find_string2(searchthrough, tofind): #Takes two strings and tries to find the content of string2 in string1, if it does it returns true otherwise false.
	try:
		result = searchthrough.find(tofind)
		if result != -1:
			#print ("found '" + tofind + "' at index: " + str(result))
			return True
	except:
		print ("failed to return")
	return False


def loopthroughitems ():
	for item in child:	#loops through all items in child and checks if both check1 and check2 is true 
		test = (item.attrib)
		check1 = find_string2(str(test), "OPENPVP_BLACK")
		check2 = find_string2(str(test), "EU_20_00")
		if check1 and check2:
			print (test['name'], test['displayname'])

#=====================================

loopthroughitems()