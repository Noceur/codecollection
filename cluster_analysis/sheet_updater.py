import gspread
import os
import re
import sys
import time
from oauth2client.service_account import ServiceAccountCredentials
from xml.etree import ElementTree


doc = 'world_live/world.xml'
doc2 = '0201_WRL_SW_T5_KPR_ROY.cluster.xml'
 
 
# use creds to create a client to interact with the Google Drive API

#scope = ['https://spreadsheets.google.com/feeds']
#creds = ServiceAccountCredentials.from_json_keyfile_name('Cluster analysis-bac77d2732de.json', scope)
#client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

#sheet = client.open("test_analysis").sheet1
 
# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
#print (sheet.get_all_values())


def loc(col, row):
	return (str(col+row))

#sheet.update_acell(loc("e", "10"), "test")




class cluster():
	def __init__(self, clusterName):
		self.clusterName = clusterName
		self.templates = []

	def add_template(self, templateName, rot, layers):
		template = {'template': templateName, 'rotation': rot, 'layers': layers}
		self.templates.append(template)

	def print_data(self):
		print (self.clusterName)
		print (self.templates)


def get_layer_name():
	pass

def add_cluster():
	pass

def upd_cell():
	pass

def main():
	if getattr(sys, 'frozen', False):
			application_path = os.path.dirname(sys.executable)
	elif __file__:
			application_path = os.path.dirname(__file__)

	clusterPath = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\shared\\gamedata\\cluster")
	templatePath = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\shared\\gamedata\\templates")


	tree = ElementTree.parse(clusterPath + "\\" + doc2)
	root = tree.getroot()
	currentCluster = cluster(doc2[:-12])

	content = {'template': "", 'rotation': "", 'layers': []}
	for item in root:
		if not item.attrib['ref'][0] == "B" or "streetcrossing" in item.attrib['ref'].lower():
			try:
				content['template'] = item.attrib['ref']
				content['rotation'] = item.attrib['rot']
			except: 
				content['template'] = item.attrib['ref']
				content['rotation'] = "0"
			for item2 in item:
				content['layers'].append(item2.attrib['id'])
			currentCluster.add_template(content['template'], content['rotation'], content['layers'])
			content = {'template': "", 'rotation': "", 'layers': []}
	currentCluster.print_data()





if __name__ == "__main__":
	main()