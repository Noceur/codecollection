from xml.etree.ElementTree import Element, SubElement, Comment
#from lxml import Element, SubElement, Comment
from ElementTree_pretty import prettify


clusters = Element("clusters")

class cluster():
	def __init__(self, cluster_name, biome):
		self.cluster = ""
		self.cluster_name = cluster_name
		self.cluster_path = ("Assets/Levels/_EXPORT/ThirdGenerationWorld/" + cluster_name + ".cluster")
		self.master = ""
		self.biome = biome
		self.layer = ""

	def add_master(self, master, layers=[]):
		self.master = SubElement(self.cluster, "master", path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Master/" + master), position="y", orientation="0")
		if not len(layers) == 0:
			self.add_layers(self.master, layers)

	def add_template(self, template, id, layers=[], rotatewithmaster=True, orientation=0):
		self.template = SubElement(self.cluster, "template", id=id, rotatewithmaster=str(rotatewithmaster), path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Slave/" + template), position="y", orientation=str(orientation))
		if not len(layers) == 0:
			self.add_layers(self.template, layers)

	def add_layers(self, template, layers=[]):
		for l in layers:
			SubElement(template, "layer", name=l)

	def append_cluster(self):
		self.cluster = SubElement(clusters, "cluster", path=self.cluster_path)



test = cluster("0001_SW", "Swamp")
test.append_cluster()
#test.add_master("002_L2_M3_S5")
test.add_master("002_L2_M3_S5", ["test", "test2"])
test.add_template("L_Mobcamp_HER_01", "L_01", ["test", "test2"])

test2 = cluster("0002_SW", "Swamp")
test2.append_cluster()
#test.add_master("002_L2_M3_S5")
test2.add_master("003_L1_M4_S5", ["test3", "test4"])
test2.add_template("L_Mobcamp_HER_03", "L_02", ["test6", "test8"])

print (prettify(clusters))

