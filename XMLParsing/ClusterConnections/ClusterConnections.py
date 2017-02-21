import lxml.etree as etree
import sys
from ElementTree_pretty import prettify

def write_to_xml(filename, towrite):
    f = open(filename, 'wb')
    f.write(etree.tostring(towrite, pretty_print=True))
    f.close()

def do_jobs(log_before=True, log_after=True):
	for job in jobs:
		print (job['ID'])
		SourceCluster = cluster(job['ID'])
		TargetCluster = cluster(job['TargetID'])
		SourceCluster.get_exits()
		TargetCluster.get_exits()

		if log_before:
			print ("\nexits before job:")
			SourceCluster.print_exits()
			TargetCluster.print_exits()

		if jobs[0]['Exit'] == 'N':
			if jobs[0]['TargetExit'] == 'N':
				print ("You are linking N to N exit(?)")
				SourceCluster.exitN.attrib['targetid'] = (TargetCluster.exitN.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitN.attrib['targetid'] = (SourceCluster.exitN.attrib['id'] + "@" + SourceCluster.clusterID)

			elif jobs[0]['TargetExit'] == 'E':
				SourceCluster.exitN.attrib['targetid'] = (TargetCluster.exitE.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitE.attrib['targetid'] = (SourceCluster.exitN.attrib['id'] + "@" + SourceCluster.clusterID)

			elif jobs[0]['TargetExit'] == 'S':
				SourceCluster.exitN.attrib['targetid'] = (TargetCluster.exitS.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitS.attrib['targetid'] = (SourceCluster.exitN.attrib['id'] + "@" + SourceCluster.clusterID)

			else:
				SourceCluster.exitN.attrib['targetid'] = (TargetCluster.exitW.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitW.attrib['targetid'] = (SourceCluster.exitN.attrib['id'] + "@" + SourceCluster.clusterID)

		elif jobs[0]['Exit'] == 'E':
			if jobs[0]['TargetExit'] == 'N':
				SourceCluster.exitE.attrib['targetid'] = (TargetCluster.exitN.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitN.attrib['targetid'] = (SourceCluster.exitE.attrib['id'] + "@" + SourceCluster.clusterID)

			elif jobs[0]['TargetExit'] == 'E':
				print ("You are linking E to E exit(?)")
				SourceCluster.exitE.attrib['targetid'] = (TargetCluster.exitE.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitE.attrib['targetid'] = (SourceCluster.exitE.attrib['id'] + "@" + SourceCluster.clusterID)

			elif jobs[0]['TargetExit'] == 'S':
				SourceCluster.exitE.attrib['targetid'] = (TargetCluster.exitS.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitS.attrib['targetid'] = (SourceCluster.exitE.attrib['id'] + "@" + SourceCluster.clusterID)

			else:
				SourceCluster.exitE.attrib['targetid'] = (TargetCluster.exitW.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitW.attrib['targetid'] = (SourceCluster.exitE.attrib['id'] + "@" + SourceCluster.clusterID)

		elif jobs[0]['Exit'] == 'S':
			if jobs[0]['TargetExit'] == 'N':
				SourceCluster.exitS.attrib['targetid'] = (TargetCluster.exitN.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitN.attrib['targetid'] = (SourceCluster.exitS.attrib['id'] + "@" + SourceCluster.clusterID)

			elif jobs[0]['TargetExit'] == 'E':
				SourceCluster.exitS.attrib['targetid'] = (TargetCluster.exitE.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitE.attrib['targetid'] = (SourceCluster.exitS.attrib['id'] + "@" + SourceCluster.clusterID)
			elif jobs[0]['TargetExit'] == 'S':
				print ("You are linking S to S exit(?)")
				SourceCluster.exitS.attrib['targetid'] = (TargetCluster.exitS.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitS.attrib['targetid'] = (SourceCluster.exitS.attrib['id'] + "@" + SourceCluster.clusterID)
			else:
				SourceCluster.exitS.attrib['targetid'] = (TargetCluster.exitW.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitW.attrib['targetid'] = (SourceCluster.exitS.attrib['id'] + "@" + SourceCluster.clusterID)

		else:
			if jobs[0]['TargetExit'] == 'N':
				SourceCluster.exitW.attrib['targetid'] = (TargetCluster.exitN.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitN.attrib['targetid'] = (SourceCluster.exitW.attrib['id'] + "@" + SourceCluster.clusterID)
			elif jobs[0]['TargetExit'] == 'E':
				SourceCluster.exitW.attrib['targetid'] = (TargetCluster.exitE.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitE.attrib['targetid'] = (SourceCluster.exitW.attrib['id'] + "@" + SourceCluster.clusterID)
			elif jobs[0]['TargetExit'] == 'S':
				SourceCluster.exitW.attrib['targetid'] = (TargetCluster.exitS.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitS.attrib['targetid'] = (SourceCluster.exitW.attrib['id'] + "@" + SourceCluster.clusterID)
			else:
				print ("You are linking W to W exit(?)")
				SourceCluster.exitW.attrib['targetid'] = (TargetCluster.exitW.attrib['id'] + "@" + TargetCluster.clusterID)
				TargetCluster.exitW.attrib['targetid'] = (SourceCluster.exitW.attrib['id'] + "@" + SourceCluster.clusterID)

		if log_after:
			print ("\nexits after job:")
			SourceCluster.print_exits()
			TargetCluster.print_exits()

def load_xml(xml):
	doc = xml
	tree = etree.parse(doc)
	root = tree.getroot()
	element = root[0]
	return element, tree

class cluster():
	def __init__(self, clusterID):
		self.clusterID = clusterID
		self.exitN = ''
		self.exitE = ''
		self.exitS = ''
		self.exitW = ''
		#print (self.clusterID)

	def get_exits(self, quiet=False):
		for item in element:
			printList = []
			exitSide = ''
			attribute = item.attrib
			for content in item:
				if attribute['id'] == self.clusterID:
					if content.tag == 'exits':
						if not quiet == True:
							print (item.tag, item.attrib['id'])
							print ('\t',content.tag)
						for exit in content:
							if exit.attrib['targettype'] == 'Cluster':
								x = float(exit.attrib['pos'].split()[0])
								y = float(exit.attrib['pos'].split()[1])

								


								if x < y and y < (x*(-1)):
									#if exit.attrib['targetid'] != "00000000-0000-0000-0000-000000000000":
										#print ("in use")
										#sys.exit(("West exit in cluster", self.clusterID, "already has GUID assigned."))
									exitSide = 'W'
									self.exitW = exit
								elif x > y and x > (y*(-1)):
									exitSide = 'E'
									self.exitE = exit
								elif y > x and y > (x*(-1)):
									exitSide = 'N'
									self.exitN = exit
								else:
									exitSide = 'S'
									self.exitS = exit




								#print ('\t\texit pos:\t', x, y, exitSide, '\t\t', exit.attrib['targetid']) 
								if not quiet == True:
									print ('\t\texit side:', exitSide,'\texit pos:', x, y, '\t\t', exit.attrib['targetid']) 
		print ("")

	def print_exits(self):
		print (self.clusterID)
		print ("\t\tEXIT N-\t\t    id:", self.exitN.attrib['id'], "\t targetid:", self.exitN.attrib['targetid'])
		print ("\t\tEXIT E-\t\t    id:", self.exitE.attrib['id'], "\t targetid:", self.exitE.attrib['targetid'])
		print ("\t\tEXIT S-\t\t    id:", self.exitS.attrib['id'], "\t targetid:", self.exitS.attrib['targetid'])
		print ("\t\tEXIT W-\t\t    id:", self.exitW.attrib['id'], "\t targetid:", self.exitW.attrib['targetid'])

jobs = [
{
	'ID':			'2204',
	'Exit':			'S',
	'TargetID':		'1203',
	'TargetExit':	'N'
},
{
	'ID':			'2204',
	'Exit':			'E',
	'TargetID':		'1203#1',
	'TargetExit':	'N'
},
{
	'ID':			'1203',
	'Exit':			'E',
	'TargetID':		'1203#1',
	'TargetExit':	'W'
},
{
	'ID':			'1203',
	'Exit':			'W',
	'TargetID':		'2211',
	'TargetExit':	'E'
},
{
	'ID':			'1203',
	'Exit':			'S',
	'TargetID':		'2215',
	'TargetExit':	'N'
},
{
	'ID':			'1203#1',
	'Exit':			'S',
	'TargetID':		'2215',
	'TargetExit':	'E'
},
{
	'ID':			'2215',
	'Exit':			'W',
	'TargetID':		'2214',
	'TargetExit':	'E'
},
{
	'ID':			'2211',
	'Exit':			'S',
	'TargetID':		'2214',
	'TargetExit':	'N'
}
]

element, tree = load_xml('world.xml')

do_jobs(False, False)

#write_to_xml('world.xml', tree)

