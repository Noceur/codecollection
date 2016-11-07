from xml.etree import ElementTree
import re

#=====================================
'''
doc = [
	'0098_SW_003_T8_UND_L_180_WLD.cluster.xml',
	'0099_SW_004_T7_UND_T_0_WLD.cluster.xml',
]
tree = ElementTree.parse(doc[0])
root = tree.getroot()
child = root[0]
#child2 = root[0][0]
'''

#=====================================

def find_string(searchthrough, tofind): #Takes two strings and tries to find the content of string2 in string1, if it does it prints the index of where it starts.
	try:
		result = searchthrough.find(tofind)
		if result != -1:
			print ("found '" + tofind + "' at index: " + str(result))
	except:
		print ("failed to return")

def find_string2(searchthrough, tofind, exactphrase=False): #Takes two strings and tries to find the content of string2 in string1, if it does it returns true otherwise false.
	try:
		if exactphrase == True:
			result = searchthrough.find(tofind, 0, len(tofind))
		elif exactphrase == False:
			result = searchthrough.find(tofind)


		if result != -1:
			#print ("found '" + tofind + "' at index: " + str(result))
			return True
	except:
		print ("failed to return")
		return False


def loopthroughitems ():
	for item in child:	#loops through all items in child and checks if both check1 and check2 is true 
		#print(item.attrib['name'])
		attribute = item.attrib
		check1 = find_string2(str(attribute), "OPENPVP_BLACK")
		check2 = find_string2(str(attribute), "EU_20_00")
		if check1 and check2:
			print (attribute['name'])#, attribute['displayname'])

def loopthroughitems2 ():
	stringtofind = "HIDE_HIGH_NODE"
	i = 0
	documentnumber = 0
	totalfound = 0
	len(doc)

	while documentnumber < len(doc):
		for item in root:	#loops through all items in child and checks if both check1 and check2 is true 
			attribute = item.attrib
			#print (attribute['name'])
			check1 = find_string2(str(attribute), stringtofind, False)
			if check1:
				i += 1
				print (stringtofind)
				#print (attribute['name'])
		print (i, "matches in", doc[documentnumber])
		documentnumber += 1
		totalfound += i
		i = 0
	#print (totalfound, "matches found in", doc[documentnumber-1], "documents.")
	print (totalfound, "matches found in", str(documentnumber), "documents.")




doc2 = [
	'world_live/world.xml',
	'world_new/world.xml',
]

tree2 = ElementTree.parse(doc2[0])
root2 = tree2.getroot()
child2 = root2[0]


def loopthroughitems3 ():
	stringtofind = "HIDE_HIGH_NODE"
	i = 0
	documentnumber = 0
	totalfound = 0
	len(doc2)


	#while documentnumber < len(doc2):
	for item in root2[0]:	#loops through all items in child and checks if both check1 and check2 is true 
		attribute = item.attrib
		#print (attribute['name'])
		#check1 = find_string2(str(attribute), stringtofind, False)
		#print (attribute)
		if attribute['type'] == "OPENPVP_BLACK" and find_string2(attribute['name'], "_HL_"):
			print (attribute['name'], "\ntrunk pos:")
			for part in item:
				for part2 in part:
					attribute2 = part2.attrib
					#print (attribute2)
					try:
						if attribute2['territorytype'] == "NORMAL" or attribute2['territorytype'] == "WATCHTOWER":
							print ("Territory type:", attribute2['territorytype'], "\nResource type:", attribute2['resourcetype'], "\ncenter pos:", attribute2['center'], "\nsize:", attribute2['size'])
					except:
						pass
						#print ("failed")
			#print (attribute['name'])
			print ()

	#print (i, "matches in", doc[documentnumber])

	documentnumber += 1
	totalfound += i
	i = 0


	#print (totalfound, "matches found in", doc[documentnumber-1], "documents.")
	print (totalfound, "matches found in", str(documentnumber), "documents.")

#=====================================

loopthroughitems3()