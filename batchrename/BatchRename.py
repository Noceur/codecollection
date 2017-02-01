import os, sys, re

def find_file_by_string(searchString, path):
	found_files = []
	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			if searchString in filename:
				found_files.append(filename)
				print (filename)
	return found_files

def rename_file(file, renameString):
	fileExt = re.findall("\..*", file) #regular expression to match anything after first ".", returns as list
	print (fileExt)
	os.rename(file, (renameString + fileExt[0]))

def batch_rename(renameList, path):
	for renameTask in renameList:
		found_files = find_file_by_string(renameTask[0], path)
		#print (found_files)
		for file in found_files:
			rename_file(file, renameTask[1])

currentPath = os.getcwd() 

taskList = [ #taskList[0] is what you want to look in the filenames for and taskList[1] is what the filename will become.
["0215", "0215_WRL_SW_T5_KPR_OUT_HIG"],
]

batch_rename(taskList, currentPath)