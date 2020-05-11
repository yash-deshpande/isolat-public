from bs4 import BeautifulSoup
import requests
import pandas
import time
import io
import json


def get_global_interventions():
	"""
	Get intervention data on  countries level
	Source: https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset
	Check https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset for meta data
	"""
	# get website content
	with requests.Session() as s:
		webpage = s.get("https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset")
		content = webpage.content
	# get link
	parser = BeautifulSoup(content, "html.parser")
	link =  "https://data.humdata.org"+parser.select('div.hdx-btn-group.hdx-btn-group-fixed >a.btn.btn-empty.btn-empty-blue.hdx-btn.resource-url-analytics.ga-download')[0]['href']
	# download and load
	df = pandas.read_excel(link, sheet_name = "Database")
	
	# change column names to lowercase, and fix  'alternative source' to 'alternative_source' for consistency
	df.columns = df.columns.str.lower()
	df=df.rename(columns = {'alternative source':'alternative_source'})
	# fix spelling mistakes
	df.loc[df['category'] == "Movement Restriction",'category'] = "Movement restrictions"
	df.loc[df['category'] == "Movement Restrictions",'category'] = "Movement restrictions"
	df.loc[df['category'] == "Social and Economic Measures",'category'] = "Social and economic measures"
	df.loc[df['category'] == "Social Distancing",'category'] = "Social distancing"
	# unifrom date format
	df.loc[:,'date_implemented'] = pandas.to_datetime(df['date_implemented']).dt.strftime('%m/%d/%y')
	df.loc[:,'entry_date'] = pandas.to_datetime(df['entry_date']).dt.strftime('%m/%d/%y')
	
	return df




	