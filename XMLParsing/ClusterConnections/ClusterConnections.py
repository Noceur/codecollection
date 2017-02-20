import lxml.etree as etree
from ElementTree_pretty import prettify

def change_elem_attrib(searchattribstring, searchattrib, changeattribstring, changeattrib):
    for item in element:
        attribute = item.attrib

        if searchattribstring in attribute[searchattrib]:
            oldData = attribute[changeattrib]
            attribute[changeattrib] = changeattribstring
            print (attribute[searchattrib])
            print (attribute[searchattrib] + "\t\t\t\told attribute value (" + changeattrib + "): " + oldData + "\t\t\t\tnew attribute value: " + changeattribstring)

def write_to_xml(filename, towrite):
    f = open(filename, 'wb')
    #print (etree.tostring(towrite, pretty_print=True))
    f.write(etree.tostring(towrite, pretty_print=True))
    f.close()

def pp(e):
    print (prettify(e))
    #print (etree.tostring(e, pretty_print=True)) 


doc = 'world.xml'
tree = etree.parse(doc)
root = tree.getroot()
element = root[0]





#change_elem_attrib("4247", "file", "00:00", "timeregion")

#print (listOfTimezones[0])
#for item in listOfTimezones:
#    change_elem_attrib(item[0], "file", item[1], "timeregion")

class cluster():
	def __init__(self, clusterID):
		self.clusterID = clusterID
		self.exitN = ""
		self.exitE = ""
		self.exitS = ""
		self.exitW = ""


	def get_exits(self):
		for item in element:
			printList = []
			exitSide = ""
			attribute = item.attrib
			for content in item:
				if attribute["id"] == self.clusterID:
					print (item.tag, item.attrib["id"])

					if content.tag == "exits":
						print ("\t",content.tag)
						for exit in content:
							if exit.attrib['targettype'] == "Cluster":
								x = float(exit.attrib['pos'].split()[0])
								y = float(exit.attrib['pos'].split()[1])

								


								if x < y and y < (x*(-1)):
									exitSide = "W"
									self.exitW = exit
								elif x > y and x > (y*(-1)):
									exitSide = "E"
									self.exitE = exit
								elif y > x and y > (x*(-1)):
									exitSide = "N"
									self.exitN = exit
								else:
									exitSide = "S"
									self.exitS = exit









								print ("\t\texit pos:\t", x, y, exitSide, "\t\t", exit.attrib['targetid']) 
								#printList.append(content[0].attrib)

					#print (test.attrib)
	print ()

	def print_exits(self):
		print (self.exitE, self.exitN, self.exitS, self.exitW)



cluster2214 = cluster("2214")
cluster2214.get_exits()

'''
for item in element:
	exitN = ""
	exitE = ""
	exitS = ""
	exitW = ""
	printList = []
	exitSide = ""
	attribute = item.attrib
	for content in item:
		if attribute["id"] == "2214":
			print (item.tag, item.attrib["id"])

			if content.tag == "exits":
				print ("\t",content.tag)
				for exit in content:
					if exit.attrib['targettype'] == "Cluster":
						x = float(exit.attrib['pos'].split()[0])
						y = float(exit.attrib['pos'].split()[1])

						


						if x < y and y < (x*(-1)):
							exitSide = "W"
							exitW = exit
						elif x > y and x > (y*(-1)):
							exitSide = "E"
							exitE = exit
						elif y > x and y > (x*(-1)):
							exitSide = "N"
							exitN = exit
						else:
							exitSide = "S"
							exitS = exit









						print ("\t\texit pos:\t", x, y, exitSide, "\t\t", exit.attrib['targetid']) 
						#printList.append(content[0].attrib)

			#print (test.attrib)
	print ()
		#print (printList)
#print (element)
#write_to_xml("world.xml", tree)
'''










write_to_xml("world2.xml", tree)


'''jobs = [
	{
		'ID': '0003',
		'Exit': 'W',
		'TargetID': '0004',
		'TargetExit': 'E'
	},
]'''
