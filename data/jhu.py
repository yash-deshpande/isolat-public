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

def getTS(datatype='confirm', region='global'):
	'''
	returns global ts for confirm, death or recovered across region = 'global' or 'US'
	'''

	URL_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
	URL_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
	URL_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

	URL_US_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
	URL_US_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'


	if region == 'global':

		if datatype == 'confirm':
			df = getdf(URL_confirmed)

		elif datatype == 'death':
			df = getdf(URL_deaths)

		elif datatype == 'recover':
			df = getdf(URL_recovered)

		else:
			print ('invalide datatype for global region, needs to be one of : confirm / death / recover \n')
			df = None

	elif region == 'US':

		if datatype == 'confirm':
			df = getdf(URL_US_confirmed)

		elif datatype == 'death':
			df = getdf(URL_US_deaths)

		else:
			print ('invalide datatype for US region, needs to be one of : confirm / death  \n')
			df = None

	else:

		print ('invalide region, should be : US or global\n')
		df = None

	return df 

