from bs4 import BeautifulSoup
import requests
import pandas
import time
import io
import json


def get_us_interventions():
	"""
	Get intervention data on  US states level
	Source: https://www.nga.org/coronavirus/
	"""
	# To pretened that we are real users .. 
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	# get webpage content
	with requests.Session() as s:
		webpage = s.get("https://www.nga.org/coronavirus/", headers = headers)
		content = webpage.content
	# get link
	parser = BeautifulSoup(content, "html.parser")
	allLinks = parser.select('div.entry-content.clearfix')[0].find_all('a')
	directory = [b['href'] for b in allLinks if 'Spreadsheet' in b.text]
	# a hacky way to make sure website layout did not change
	assert len(directory) == 1
	link =  directory[0]
	# read url
	with requests.Session() as s:
		data = s.get(link, headers = headers)
	# download data
	df = pandas.read_excel(io.BytesIO(data.content))
	#standard states names
	df.loc[:,'State'] = df.State.str.split('(').str[0].str[:-1]
	df.loc[df.State =='CNMI','State'] = 'Northern Mariana Islands'
	
	return df

