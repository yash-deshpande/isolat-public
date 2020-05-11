## HOW TO USE THESE DATA FILES ##


# JHU data

from jhu import getTS

# Global

# confirmed cases as data-frame
df_confirm = getTS(datatype='confirm', region='global')

# deaths as data-frame
df_death = getTS(datatype='death', region='global')

# recovered as data-frame
df_recover = getTS(datatype='recover', region='global')


# US

# confirmed cases as data-frame
df_US_confirm = getTS(datatype='confirm', region='US')

# deaths as data-frame
df_US_death = getTS(datatype='death', region='US')


# save data-frame as CSV to a file

df_confirm.to_csv('/tmp/confirmed.csv', encoding='utf-8', index=False)


# Beoutbreakprepared data

from beoutbreakprepared import getTS

# timeseries data
df_timeseries = getTS(datatype='timeseries')

# demographic data
df_demographic = getTS(datatype='demographic')


# please run "pip install -r requirements.txt" (a level above this directory, in case the lines below do not execute)

# NGA intervention data
from nga import get_us_interventions
# get  US states interventions information.
us_interventions_df  = get_us_interventions()


# HDX global intervention data


from hdx import get_global_interventions
# get (timestamped) global (conutries level) interventions
global_intervention_df = get_global_interventions()



# UNACAST data 
from unacast import get_social_distancing
# get (timestamped) social distancing grades for state-level (>30 days, 51 states)
social_distancing_state_df = get_social_distancing(level = 'state')
# get (timestamped) social distancing grades for county-level (2 days, 1955 counties)
social_distancing_county_df = get_social_distancing(level = 'county')

# NYTimes data

import nytimes

# get raw dataframes of state- and county- wise cases
raw_states_df, raw_county_df = nytimes.get_nyt_data()

# convert these into (typically more useful) time series of state or county-wise cases/deaths
# examples of state wise confirmed cases, and county wise deaths
state_cases_ts = nytimes.convert_state_df_to_ts(raw_states_df, quantity = 'cases')
county_deaths_ts = nytimes.convert_county_df_to_ts(raw_county_df, quantity = 'deaths')

# Covid Tracking Project data
import covidtrackingproject

# get dataframes from Covid Tracking Project as a dictionary
dict_dfs_covid_tracking_project = covidtrackingproject.get_covid_tracking_data()
# unpack some of them as dataframe variables. Run dict_dfs_covid_tracking_project.keys() to see
# the full list available.
states_current_df = dict_dfs_covid_tracking_project['states_current']
states_historical_df = dict_dfs_covid_tracking_project['states_historical']
us_current_df = dict_dfs_covid_tracking_project['us_current']
us_historical_df = dict_dfs_covid_tracking_project['us_historical']
# convert one of these into a time series 
states_historical_hospitalized_ts = nytimes.convert_state_df_to_ts(states_historical_df, quantity='hospitalized')

# the following might be useful to give an initial sense of the data
states_historical_df.head()


# Kinsa Health data

import kinsa

#default usage, get all states data
kinsa_df = kinsa.get_kinsa_data()
# pulling specific states
kinsa_ca_df = kinsa.get_kinsa_data(['CA'])
kinsa_tristate_df = kinsa.get_kinsa_data(['NY', 'NJ', 'CT'])
# kinsa_df: Dataframe of kinsa data. Check kinsa_df.head() and following link for more info
# https://content.kinsahealth.com/covid-detection-technical-approach for methodology

# State-wise data from India

import india

#default usage
india_df = india.get_india_data()
# pulls data from https://prsindia.org/covid-19/cases


# Google Mobility Data (time series)

from google_mobility import get_google_mobility_ts

# pulls data from https://covid19-analysis.netlify.app

# Global level data
google_global = get_google_mobility_ts(region = 'global')
# US level data
google_us = get_google_mobility_ts(region = 'US')
