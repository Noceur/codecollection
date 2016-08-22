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
		test = (item.attrib) #dict
		#testfind = item.fintext(('cluster').attrib('name'))
		check1 = find_string2(str(test), "OPENPVP_BLACK")
		check2 = find_string2(str(test), "EU_20_00")
		if check1 and check2:
			#print (test)
			print (test['name'], test['displayname'])
			#print (test['displayname\n'] + "\n")
			#if test.has_key('name')
			#if d.has_key('key'):
 			#print d['key']
			#print (testfind)

#=====================================

#loopthroughitems()




testfind = tree.find('.//cluster').attrib['name']
print (testfind)

testfind2 = tree.find('.//cluster').attrib['displayname']
print (testfind2)










if tree.findall('.//cluster'):
	test = tree.find('.//cluster')
	print (test)

'''for node in tree.find('clusters'):
    print node.attrib['cluster']
    # Create sub elements
    if node.attrib['topic']=="sys/phoneNumber/1":
        tag = SubElement(node,'TagName')
        tag.attrib['attr'] = 'AttribValue'
        '''


#for item in child:
#	print(item.attrib)




#findthis = root.find('name')

'''try:
	print (findthis.attrib)
except:
	print ("fail")'''


#print (root[0])
#print (cofcofroot)
#test = root.child.tag
#test2 = test.child.tag
#print (root.attrib)
#print (test)
#print (test2)

#print (cofcofroot.attrib)
#print (cofcofroot.attrib)

#for child in root:
#	print(child.tag)