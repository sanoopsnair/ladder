#!/usr/bin/python
import sys
import os
import yaml   #sudo pip install PyYAML
import ast

params = str(sys.argv)
params = ast.literal_eval(params)

# Function to read config file
def readConfig():
	with open('config.yaml', 'r') as f:
		doc = yaml.load(f)
	return doc
configData = readConfig()

# Find data from config file
def findData(params=None):
	if params:
		for eachData in configData:
			if params in configData[eachData].values():
				return configData[eachData]
			else:
				pass
	else:
		print "no params in findData"
		

# Function to create script 
def createScript(params=None):
	if params:
		findedData = findData(params)
		if len(findedData) > 1:
			script = "sudo ssh -i bucket/"+findedData['pemFile']+" "+findedData['ip']
			os.system(script)
	else:
		print "no params in createScript"


if len(params) > 1:
	createScript(params[1])
else:
	for eachData in configData:
		print configData[eachData]['aliasName']
