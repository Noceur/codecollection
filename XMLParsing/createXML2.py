from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify




clusters = Element("clusters")





def add_cluster(clustername):
	cluster = SubElement(clusters, "cluster", path="PATH", )

	Template = SubElement(clusters, "a")

	


print (prettify(clusters))