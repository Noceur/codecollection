import gspread
import os
import re
import sys
import time
from oauth2client.service_account import ServiceAccountCredentials
from xml.etree import ElementTree


no_data_added = True
 
 
# google API credentials
# ===================================================


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Cluster analysis-bac77d2732de.json', scope)
client = gspread.authorize(creds)

sheet = client.open("cluster_analysis").sheet1


# ===================================================

row_count = 1


class cluster():
	def __init__(self, clusterName):
		self.clusterName = clusterName
		self.templates = []
		self.formatForUpload = []

	def add_template(self, templateName, rot, layers):
		template = {'template': templateName, 'rotation': rot, 'layersId': layers, 'layersName': []}
		self.templates.append(template)

	def template_id_switch(self):
		for template in self.templates:
				try:
					for layer in template['layersId']:
						#print (template['layersName'])
						#print (template['template'])
						#print (layer)
						#template['layersName'].append(get_layer_name(template['template'], layer))
						#layer = get_layer_name(template['template'], layer)
						template['layersName'].append(get_layer_name(template['template'], layer))
				except:
					continue

	def print_data(self):
		print (self.clusterName)
		#print (self.templates)
		for item in self.templates:
			print (item['template'])
			print (item['rotation'])
			print (item['layersName'])
			print ()
		#print (self.templates)

	def format_for_upload(self):
		dataToAdd = []
		dataToAdd.append(self.clusterName)
		dataToAdd.append("")
		dataToAdd.append("")
		dataToAdd.append("")
		self.formatForUpload.append(dataToAdd)
		dataToAdd = []
		try:
			for template in self.templates:
				#layers = ""
				dataToAdd.append("")
				dataToAdd.append(template['template'])
				dataToAdd.append(template['rotation'])
				if len(template['layersName']) > 0:
					dataToAdd.append(template['layersName'])
					#for layer in template['layersName']:
					#	dataToAdd.append(layer)	
				else:
						dataToAdd.append("")
				self.formatForUpload.append(dataToAdd)
				dataToAdd = []
		except:
			print ("no templates to add in this cluster?")

		for each in self.formatForUpload:
			print (each)
		


def get_layer_name(template, layerid):
	if getattr(sys, 'frozen', False):
		application_path = os.path.dirname(sys.executable)
	elif __file__:
		application_path = os.path.dirname(__file__)

	templatePath = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\shared\\gamedata\\templates")

	templ_tree = ElementTree.parse(templatePath + "\\" + template + ".template.xml")
	templ_root = templ_tree.getroot()
	for item in templ_root:
		for item2 in item:
			if not "tile" in item2.tag:
				for item3 in item2:
					#print (item3.attrib['name'])
					try:
						#print (item3.attrib['name'])
						if layerid == item3.attrib['id']:
							return item3.attrib['name']
					except: 
						continue
	return "LayerId incorrect(?)"


def add_cluster(clusterdata):
	#TODO Use v to find which position to use with sheet.range.
	'''
	gspread.utils.rowcol_to_a1(row, col)
	Translates a row and column cell address to A1 notation.
	
	Parameters:	
	row – The row of the cell to be converted. Rows start at index 1.
	col – The column of the cell to be converted. Columns start at index 1.
	Returns:	
	a string containing the cell’s coordinates in A1 notation.
	
	Example:
	
	>>> rowcol_to_a1(1, 1)
	A1
	'''


	# Select a range

	#cell_list = sheet.range('A1:C7')
	#print (cell_list)
	#for cell in cell_list:
	#	print (cell)
	#	cell.value = 'test'
	#test = sheet.cell(5,5)
	#
	#test.value = 'derp'
	#
	#sheet.update_cells(test)
	print (row_count+len(clusterdata.formatForUpload))
	x = row_count+len(clusterdata.formatForUpload)
	rangeFrom = colrow_to_A1(1, row_count+1)
	rangeTo = colrow_to_A1(4, (row_count+len(clusterdata.formatForUpload)))
	flattened = []
	#print (str(rangeFrom + ":" + rangeTo))
	#clusterDataFlat = flatten(clusterdata.formatForUpload)
	for item in clusterdata.formatForUpload:
		for item2 in item:
			flattened.append(item2)

	#print (flattened)
	#print (clusterDataFlat)

	cell_list = sheet.range(str(rangeFrom + ":" + rangeTo))
	for thing, cell in zip(flattened, cell_list):
		print (cell)
		cell.value = thing

	print (cell_list)

	sheet.update_cells(cell_list)
	#row_count + len(clusterdata.formatForUpload)

	# Update in batch
	#sheet.update_cells(cell_list)



	#column_count = 0
	#if no_data_added == True:
	#	sheet.update_cell(1,1, "cluster ID")
	#	x = 0
	#	while x <= 4:
	#		sheet.update_cell(1,((x*3)+2), "template")
	#		sheet.update_cell(1,((x*3)+3), "rotation")
	#		sheet.update_cell(1,((x*3)+4), "layers")
	#		x += 1


def populate_cluster_list(loc):
	f = []
	output = []
	for (dirpath, dirnames, filenames) in os.walk(loc):
		f.extend(filenames)
	for file in f:
		if "WRL" in file and not ".txt" in file:
			output.append(file)
	for entry in output:
		print (entry)
	return output

def colrow_to_A1(col, row):
    return numberToLetters(col)+str(row)

def numberToLetters(q):
    """
    Helper function to convert number of column to its index, like 10 -> 'A'
    """
    q = q - 1
    result = ''
    while q >= 0:
        remain = q % 26
        result = chr(remain+65) + result;
        q = q//26 - 1
    return result

def upd_acell(col, row, data):
	sheet.update_acell(str(col+row), data)


def main():
	if getattr(sys, 'frozen', False):
			application_path = os.path.dirname(sys.executable)
	elif __file__:
			application_path = os.path.dirname(__file__)

	clusterPath = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\shared\\gamedata\\cluster")
	templatePath = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\shared\\gamedata\\templates")

	clusterList = populate_cluster_list(clusterPath)

	global row_count

	for clusterEntry in clusterList:

		tree = ElementTree.parse(clusterPath + "\\" + clusterEntry)
		root = tree.getroot()
		currentCluster = cluster(clusterEntry[:-12])

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
		currentCluster.template_id_switch()
		#currentCluster.print_data()
		#print (get_layer_name("SW_focusMOB_01", "Layer_02"))
		#sheet.update_cell(5,5,"test")
		currentCluster.format_for_upload()
		add_cluster(currentCluster)
		row_count += len(currentCluster.formatForUpload)


if __name__ == "__main__":
	main()