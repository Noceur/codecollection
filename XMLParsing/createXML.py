# CSV module
from bs4 import BeautifulSoup
import csv
# Stuff from the XML module
from xml.etree.ElementTree import Element, SubElement, tostring
from ElementTree_pretty import prettify

# Topmost XML element
top = Element('clusters')
# Open a file
with open("D:/Git/backup/codecollection/XMLParsing/export.csv") as csvfile:
    # And use a dictionary-reader
    reader = csv.DictReader(csvfile)
    for d in reader:
        # For each mapping in the dictionary
        for (k, v) in d.items():
            # Create an XML node
            child = SubElement(top, k)
            child.text = v
print (tostring(top))



x = "clusters.xml"

print(BeautifulSoup(x, "xml").prettify())