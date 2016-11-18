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


testlist = [['test', 'Forest'], ['201_L1_M3_S5', '0']]#, ['route 1', 'route 2', 'route 3', 'route 4', 'route 5']]]


def break_down_list(clusterlist):
	cluster_object = cluster(clusterlist[0][0], clusterlist[0][1])
	cluster_object.append_cluster() 
	try: 
		cluster_object.add_master(clusterlist[1][0], clusterlist[1][1], clusterlist[1][2])
	except:
		print ("\n########################################\nLayers are missing in master template yo\n########################################\n")
		sys.exit(0)

	


	testing = []
	for n in clusterlist[1]:
		testing.append(n)
		print(testing)

	for n in clusterlist[]
	cluster_object.add_template()






	#cluster = clusterlist[0][0]
	#print = (cluster)
	#exec(cluster)

	#vars()['cluster'] = clusterlist


	#print (test)

break_down_list(testlist)

test = cluster("0001_SW", "Swamp")
test.append_cluster()
#test.add_master("002_L2_M3_S5")
test.add_master("002_L2_M3_S5", "0", ["test", "test2"])
test.add_template("L_Mobcamp_HER_01", "L_01", "0", ["test", "test2"])
#
#test2 = cluster("0002_SW", "Swamp")
#test2.append_cluster()
##test.add_master("002_L2_M3_S5")
#test2.add_master("003_L1_M4_S5", 0, ["test3", "test4"])
#test2.add_template("L_Mobcamp_HER_03", "L_02", 0, ["test6", "tsta"])
#test2.add_template("L_Mobcamp_HER_02", "L_01", 0, ["2", "s"])
#test2.add_template("L_Mobcamp_HER_01", "L_03", 0, ["v", "9"])


print (prettify(clusters))

