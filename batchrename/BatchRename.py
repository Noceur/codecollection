import os, sys, re

currentPath = os.getcwd()

def find_file_by_string(searchString):
	found_files = []
	for root, dirs, filenames in os.walk(currentPath):
		for filename in filenames:
			if searchString in filename:
				found_files.append(filename)
				print (filename)
	return found_files

def rename_file(file, renameString):
	fileExt = re.findall("\..*", file) #regular expression to match anything after first ".", returns as list
	print (fileExt)
	os.rename(file, (renameString + fileExt[0]))

def batch_rename(renameList):
	for renameTask in renameList:
		found_files = find_file_by_string(renameTask[0])
		print (found_files)
		for file in found_files:
			rename_file(file, renameTask[1])

taskList = [
["4245", "4245_WRL_MN_T5_KPR_OUT"]
]

bath_rename(taskList)


#found_files = find_file_by_string("4245")
#print (found_files)
#rename_file(found_files[0], "test")