
from lxml import etree as ET

x = "PATH_TO_TEMPLATE"
n = 10
i = 0

clusters = ET.Element("clusters")

def test():
	i = 0
	cluster = ET.SubElement(clusters, "cluster")
	master = ET.SubElement(cluster, "master", path=x, position="0 0 0", orientation="0")
	layer = ET.SubElement(master, "layer", name="route_1")
	layer2 = ET.SubElement(master, "layer", name="route_2")
	template =ET.SubElement(cluster, "template", path=x, orientation="0")

	while n > i:
		i+=1
		layer = ET.SubElement(master, "layer", name=("route_" + str(i)))

test()
test()

tree = ET.ElementTree(clusters)


parser = ET.XMLParser(remove_blank_text=True)
tree.write("test.xml", pretty_print=True)