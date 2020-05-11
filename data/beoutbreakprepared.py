import requests
import pandas as pd 
import numpy as np
from dateutil import parser
import io

def getdf(URL):

	s = requests.get(URL).content
	df = pd.read_csv(io.StringIO(s.decode('utf-8')))

	return df 

def getcsv(URL, filename = '/tmp/csvfile.csv'):

	df = getdf(URL)
	df.to_csv(filename, encoding='utf-8', index=False)

	return filename


# Global / CSSEGISandData

def getTS(datatype='timeseries'):
	'''
	returns dataframe that is either timeseries or demographics.
	'''

	URL_latest = 'https://raw.githubusercontent.com/beoutbreakprepared/nCoV2019/master/latest_data/latestdata.csv'
	URL_demographic = 'https://raw.githubusercontent.com/beoutbreakprepared/nCoV2019/master/demographics/IHME_GBD_2017_POP_2015_2017_Y2018M11D08.CSV'

	if datatype == 'timeseries':
		df = getdf(URL_latest)
		return df 

	elif datatype == 'demographic':
		df = getdf(URL_demographic)
		return df 

	else:
		print ('invalide datatype, should be : timeseries or demographic\n')
		df = None

	return df



