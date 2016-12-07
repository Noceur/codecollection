from xml.etree.ElementTree import Element, SubElement, Comment
#from lxml import Element, SubElement, Comment
from ElementTree_pretty import prettify
import sys
import csv
import ast

errors = []

class cluster():
	def __init__(self, cluster_name, biome):
		self.cluster = ""
		self.cluster_name = cluster_name
		self.cluster_path = ("Assets/Levels/_EXPORT/ThirdGenerationWorld/" + cluster_name + ".unity")
		self.master = ""
		self.biome = biome
		self.layer = ""

	def add_master(self, master, orientation='0', layers=[], pos="0 0 0"):
		self.master = SubElement(self.cluster, "master", path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Master/" + master + ".unity"), position=pos, orientation=orientation)
		if not len(layers) == 0:
			self.add_layers(self.master, layers)

	def add_template(self, template, id, orientation='0', layers=[], rotatewithmaster="true"):
		self.template = SubElement(self.cluster, "template", id=id, rotatewithmaster=rotatewithmaster, path=("Assets/Levels/LEVEL_TEMPLATES/WORLD/" + self.biome + "/Slave/" + template + ".unity"), orientation=orientation)
		if not len(layers) == 0:
			self.add_layers(self.template, layers)

	def add_layers(self, template, layers=[]):
		for l in layers:
			SubElement(template, "layer", name=l)

	def append_cluster(self):
		self.cluster = SubElement(clusters, "cluster", path=self.cluster_path)

def break_down_list(clusterlist):
	number_of_templates = len(clusterlist)-2

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
		#if len(t) == 0:
		#	
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

clusters = Element("clusters")

#with open('filename.csv') as csvfile:
#	csvreader = csv.reader(csvfile)
#	for row in csvreader:
#		break_down_list(ast.literal_eval((row[0])))

		#break_down_list(row[0])
		#to_list = list(row[0])
		#to_list = to_list[:-1]

		#break_down_list(to_list)
		#to_list = row[0]
		#print (to_list)


testlist5 = [['cluster_ID6', 'Swamp'], ['001_L1_M3_S5', '90', ['route_01_on', 'route_03_on', 'route_04_on', 'route_07_on', 'route_08_on', 'route_02_off', 'route_05_off', 'route_06_off',]], ['B_SW_Corner_01', 'B_01', '270', ['swamp_swamp_01']], ['B_SW_Straight_01', 'B_02', '0', ['swamp_02']], ['B_SW_Exit_01', 'B_03', '0', ['guardtower_outland_01']], ['B_SW_Straight_01', 'B_04', '0', ['swamp_02']], ['B_SW_Corner_01', 'B_05', '0', ['swamp_swamp_01']], ['B_SW_Straight_01', 'B_06', '90', ['swamp_02']], ['B_SW_Straight_01', 'B_07', '90', ['swamp_02']], ['B_SW_Straight_01', 'B_08', '90', ['swamp_02']], ['B_SW_Corner_01', 'B_09', '90', ['swamp_swamp_01']], ['B_SW_Straight_01', 'B_10', '180', ['swamp_02']], ['B_SW_Exit_01', 'B_11', '180', ['swamp_01']], ['B_SW_Straight_01', 'B_12', '180', ['swamp_02']], ['B_SW_Corner_01', 'B_13', '180', ['swamp_swamp_01']], ['B_SW_Straight_01', 'B_14', '270', ['swamp_01']], ['B_SW_Exit_01', 'B_15', '270', ['swamp_01']], ['B_SW_Straight_01', 'B_16', '270', ['swamp_02']],['SW_StreetCrossing', 'C_01', '180', ['route_I_01'], 'true'], ['SW_StreetCrossing', 'C_02', '0', ['NONE'], 'true'], ['SW_StreetCrossing', 'C_03', '180', ['route_L_01'], 'true'], ['SW_StreetCrossing', 'C_04', '180', ['route_T_01'], 'true']]

break_down_list(testlist5)


print (prettify(clusters))
xml_file = open("cluster_generation.xml", "w")
xml_file.write(prettify(clusters))
xml_file.close()
#tree.write("filename.xml")

for e in errors:
	print (e)