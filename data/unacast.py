from bs4 import BeautifulSoup
import requests
import pandas
import time
import io
import json



def get_social_distancing(level = 'state'):
	"""
	Get social distancing score for US states and counties
	Source: https://www.unacast.com/covid19/social-distancing-scoreboard
	Parameters:
		level(str): either 'state' or 'county' (default: state) 
	"""
	# request url
	url_county_req = 'https://uc-data-portal.appspot.com/api/open/search/covidcountyaggregatestwolastdays_v2?size=4000'
	url_state_req = 'https://uc-data-portal.appspot.com/api/open/search/covidstateaggregates_v2?size=10000'

	# if level is state, return state information 
	if level == 'state':
		# get response
		with requests.Session() as s:
			response_state = s.get(url_state_req).content
		# load as json
		json_state = json.loads(response_state)
		info = []
		# loop over states
		for state in json_state['hits']['hits']:
			stateName = state['_source']['stateName']
			stateFips = state['_source']['stateFips']
			# loop over days
			for day in state['_source']['data']:
				date = day['date']
				vistation_grade = day['visitationGrade']
				totalGrade = day['totalGrade']
				travelDistanceGrade =  day['travelDistanceGrade']
				info.append([date, stateName, stateFips, vistation_grade, travelDistanceGrade, totalGrade])
		df = pandas.DataFrame(info, columns = ['date', 'state_name', 'state_fips', 'vistation_grade', 'travel_distance_grade', 'total_grade'])
		df.loc[:,'date'] = pandas.to_datetime(df['date']).dt.strftime('%m/%d/%y')
	# if level is county, return county information 
	elif level == 'county':
		# get response
		with requests.Session() as s:
			response_county = s.get(url_county_req).content
		# load as json
		json_county = json.loads(response_county)
		info = []
		# loop over counties
		for county in json_county['hits']['hits']:
			countyName = county['_source']['countyName']
			countyFips = county['_source']['countyFips']
			# loop over days
			for day in county['_source']['data']:
				date = day['date']
				vistation_grade = day['visitationGrade']
				totalGrade = day['totalGrade']
				travelDistanceGrade =  day['travelDistanceGrade']
				info.append([date, countyName, countyFips, vistation_grade, travelDistanceGrade, totalGrade])
		df = pandas.DataFrame(info, columns = ['date', 'county_name', 'county_fips', 'vistation_grade', 'travel_distance_grade', 'total_grade'])
		df.loc[:,'date'] = pandas.to_datetime(df['date']).dt.strftime('%m/%d/%y')
	# if level is not 'state' nor 'county', return value error 
	else: 
		raise ValueError ("level must either be 'state' or 'county'")
	
	return df	

