## Downloading data sets and saving output as CSV ##

# Simple function to save data frame as CSV
def save_as_csv(df, name, source, path):
    filename = path + '/' + source + '_' + name + '.csv'
    df.to_csv(filename, encoding='utf-8', index=False)

# ----------------------- #
#  Back up last data set  #
# ----------------------- #

import os, sys
from datetime import datetime

data_dir = "../data_csv"
backup_dir = data_dir + '_' + datetime.now().strftime("%Y%m%d_%H%M%S")

try:
    os.rename(data_dir, backup_dir)
    print('Previous data folder backed up successfully as ' + backup_dir)
except:
    print('No previous data folder')

try:
    os.mkdir(data_dir)
    print('Created new data folder ' + data_dir)
except:
    print('Warning: Data folder ' + data_dir + ' already exists!')


# ---------- #
#  JHU data  #
# ---------- #

from jhu import getTS

source = 'jhu'
print('Downloading jhu data')


# GLOBAL #

# confirmed cases as data-frame
df_confirm = getTS(datatype='confirm', region='global')
save_as_csv(df_confirm, 'global_confirmed', source, data_dir)

# deaths as data-frame
df_death = getTS(datatype='death', region='global')
save_as_csv(df_death, 'global_deaths', source, data_dir)

# recovered as data-frame
df_recover = getTS(datatype='recover', region='global')
save_as_csv(df_recover, 'global_recovered', source, data_dir)

# US #

# confirmed cases as data-frame
df_US_confirm = getTS(datatype='confirm', region='US')
save_as_csv(df_US_confirm, 'us_confirmed', source, data_dir)

# deaths as data-frame
df_US_death = getTS(datatype='death', region='US')
save_as_csv(df_US_death, 'us_deaths', source, data_dir)

# ------------------------- #
#  Beoutbreakprepared data  #
# ------------------------- #

from beoutbreakprepared import getTS

source = 'beoutbreakprepared'
print('Downloading beoutbreakprepared data')

# timeseries data
df_timeseries = getTS(datatype='timeseries')
save_as_csv(df_timeseries, 'timeseries', source, data_dir)

# demographic data
df_demographic = getTS(datatype='demographic')
save_as_csv(df_demographic, 'demographic', source, data_dir)

# ----------------------- #
#  NGA intervention data  #
# ----------------------- #

from nga import get_us_interventions

source = 'nga'
print('Downloading nga data')

# get  US states interventions information.
us_interventions_df  = get_us_interventions()
save_as_csv(df_demographic, 'us_interventions', source, data_dir)

# ------------------------------ #
#  HDX global intervention data  #
# -----------------------------  #

from hdx import get_global_interventions

source = 'hdx'
print('Downloading hdx data')

# get (timestamped) global (conutries level) interventions
global_intervention_df = get_global_interventions()
save_as_csv(global_intervention_df, 'global_interventions', source, data_dir)

# -------------- #
#  UNACAST data  #
# ---------------#

from unacast import get_social_distancing

source = 'unacast'
print('Downloading unacast data')

# get (timestamped) social distancing grades for state-level (>30 days, 51 states)
social_distancing_state_df = get_social_distancing(level = 'state')
save_as_csv(social_distancing_state_df, 'state_social_distancing', source, data_dir)

# get (timestamped) social distancing grades for county-level (2 days, 1955 counties)
social_distancing_county_df = get_social_distancing(level = 'county')
save_as_csv(social_distancing_county_df, 'county_social_distancing', source, data_dir)


# -------------- #
#  NYTimes data  #
# -------------- #

import nytimes

source = 'nytimes'
print('Downloading nyt data')

# get raw dataframes of state- and county- wise cases
raw_states_df, raw_county_df = nytimes.get_nyt_data()
save_as_csv(raw_states_df, 'state_raw', source, data_dir)
save_as_csv(raw_county_df, 'county_raw', source, data_dir)

# Also save in time series format mirroring what's been done in the python code
# for key in raw_states_df.keys() :
#     if key != 'date' :
#         tmp_df = nytimes.convert_state_df_to_ts(raw_states_df, quantity = key)
#         save_as_csv(tmp_df, key, source, data_dir)
#
# for key in raw_county_df.keys() :
#     if key != 'date' :
#         tmp_df = nytimes.convert_county_df_to_ts(raw_county_df, quantity = key)
#         save_as_csv(tmp_df, key, source, data_dir)

# ----------------------------- #
#  Covid Tracking Project data  #
# ----------------------------- #

import covidtrackingproject

source = 'covidtrackingproject'
print('Downloading covid tracking project data')

# get dataframes from Covid Tracking Project as a dictionary
dict_dfs_covid_tracking_project = covidtrackingproject.get_covid_tracking_data()
for key in dict_dfs_covid_tracking_project.keys() :
    save_as_csv(dict_dfs_covid_tracking_project[key], key, source, data_dir)

# ------------------- #
#  Kinsa Health data  #
# ------------------- #

import kinsa

source = 'kinsa'
print('Downloading kinsa data')

# kinsa_df: Dataframe of kinsa data. Check kinsa_df.head() and following link for more info
# https://content.kinsahealth.com/covid-detection-technical-approach for methodology

# get all states:
kinsa_df = kinsa.get_kinsa_data()
save_as_csv(kinsa_df, 'full', source, data_dir)

print('Data download and output completed')
