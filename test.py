import urllib.request
from urllib.request import *

import json

class BraVaPy():
	def __init__(self, url):
		self.url = url
			
	def metadata(self):
		metaData = []
		results = []
		try:
			data = urllib.request.urlopen(self.url)
			if data:
				data_json = json.loads(data.read())			
			
				for i in data_json['metadata']:
					metaData.append(i)
		except urllib.error.HTTPError as e:
			return ('Invalid URL: ' + str(e.code))
		return metaData
	
	def insights(self):
		metaData = []
		result = []
		results = []
		try:
			data = urllib.request.urlopen(self.url)
			if data:
			
				data_json = json.loads(data.read())			
			
				for i in data_json['metadata']:
					metaData.append(i)
					
				for j in data_json['result']:
					result.append(j)	
				
		except urllib.error.HTTPError as e:
			print('Invalid URL: ' + str(e.code))
		
		print('metadata: ')
		var = [print('--'+i) for i in metaData]
		
		print('result: ')
		var = [print('--'+j) for j in result]
		
url = 'https://webapps.ipk-gatersleben.de/api/brapi/v1/germplasm-search'
url1 = 'https://www.overleaf.com/learn/latex/Code_listinga'
'''
try:
	x=urllib.request.urlopen('https://webapps.ipk-gatersleben.de/api/brapi/v1/germplasm-search')
	
	saveFile=open('header.txt', 'w')
	saveFile.write(str(x.read()))
	saveFile.close()
except Exception as e:
	print(str(e))
'''
germplasm = BraVaPy(url)
#a = [print(i) for i in germplasm.metadata()]
#print('='*30)

germplasm.insights()

data = urlopen(url1)

#print(data.read())


