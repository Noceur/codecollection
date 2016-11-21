from xml.etree.ElementTree import Element, SubElement, Comment
#from lxml import Element, SubElement, Comment
from ElementTree_pretty import prettify
import sys

clusters = Element("clusters")

class cluster():
	def __init__(self, cluster_name, biome):
		self.cluster = ""
		self.cluster_name = cluster_name
		self.cluster_path = ("Assets/Levels/_EXPORT/ThirdGenerationWorld/" + cluster_name + ".cluster")
		self.master = ""
		self.biome = biome
		self.layer = ""

	def add_master(self, master, orientation='0', layers=[], pos="0 0 0"):
		self.master = SubElement(self.cluster, "master", path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Master/" + master), position=pos, orientation=orientation)
		if not len(layers) == 0:
			self.add_layers(self.master, layers)

	def add_template(self, template, id, orientation='0', layers=[], rotatewithmaster="true"):
		self.template = SubElement(self.cluster, "template", id=id, rotatewithmaster=rotatewithmaster, path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Slave/" + template), orientation=orientation)
		if not len(layers) == 0:
			self.add_layers(self.template, layers)

	def add_layers(self, template, layers=[]):
		for l in layers:
			SubElement(template, "layer", name=l)

	def append_cluster(self):
		self.cluster = SubElement(clusters, "cluster", path=self.cluster_path)


testlist = [['test', 'Forest'], ['201_L1_M3_S5', '0', ['route 1', 'route 2', 'route 3', 'route 4', 'route 5']], ["L_Mobcamp_HER_02", "L_01", "0", ["test", "test2"], "false"], ["L_Mobcamp_HER_02", "L_03", "4", ["test", "test2"]]]
testlist2 = [['asd', 'Swamp'], ['asd', '76', ['route 1', 'route 2', 'route 3', 'route 4', 'route 5']], ["dgddgj", "L_08", "0", ["test", "test2"], "false"], ["isduosifd", "L_03", "4", ["test", "test2"]]]

def break_down_list(clusterlist):
	number_of_templates = len(testlist)-2
	#print (number_of_templates)


	cluster_object = cluster(clusterlist[0][0], clusterlist[0][1])
	cluster_object.append_cluster() 

	if len(clusterlist[1]) == 1:
		cluster_object.add_master(clusterlist[1][0])
	elif len(clusterlist[1]) == 2:
		cluster_object.add_master(clusterlist[1][0], clusterlist[1][1])
	elif len(clusterlist[1]) == 3:
		cluster_object.add_master(clusterlist[1][0], clusterlist[1][1], clusterlist[1][2])
	elif len(clusterlist[1]) == 4:
		cluster_object.add_master(clusterlist[1][0], clusterlist[1][1], clusterlist[1][2], clusterlist[1][3])
	else:
		print ("\n########################################\nLayers are missing in master template yo\n########################################\n")
		sys.exit(0)

	#try: 
	#	cluster_object.add_master(clusterlist[1][0], clusterlist[1][1], clusterlist[1][2])
	#except:
	#	print ("\n########################################\nLayers are missing in master template yo\n########################################\n")
	#	sys.exit(0)
		
	for t in clusterlist[2:]:
		if len(t) == 3:
			cluster_object.add_template(t[0], t[1], t[2])
		elif len(t) == 4:
			cluster_object.add_template(t[0], t[1], t[2], t[3])
		elif len(t) == 5:
			cluster_object.add_template(t[0], t[1], t[2], t[3], t[4]) 
		else:
			print ("\n########################################\nIncorrect amount of arguments in the template list\n########################################\n")

		


	


	#testing = []
	#for n in clusterlist[1]:
	#	testing.append(n)
	#	print(testing)



	#for n in clusterlist[]
	#cluster_object.add_template()






	#cluster = clusterlist[0][0]
	#print = (cluster)
	#exec(cluster)

	#vars()['cluster'] = clusterlist


	#print (test)

break_down_list(testlist)
break_down_list(testlist2)

#test = cluster("0001_SW", "Swamp")
#test.append_cluster()
##test.add_master("002_L2_M3_S5")
#test.add_master("002_L2_M3_S5", "0", ["test", "test2"])
#test.add_template("L_Mobcamp_HER_01", "L_01", "0", ["test", "test2"])
#
#test2 = cluster("0002_SW", "Swamp")
#test2.append_cluster()
##test.add_master("002_L2_M3_S5")
#test2.add_master("003_L1_M4_S5", 0, ["test3", "test4"])
#test2.add_template("L_Mobcamp_HER_03", "L_02", 0, ["test6", "tsta"])
#test2.add_template("L_Mobcamp_HER_02", "L_01", 0, ["2", "s"])
#test2.add_template("L_Mobcamp_HER_01", "L_03", 0, ["v", "9"])


print (prettify(clusters))

