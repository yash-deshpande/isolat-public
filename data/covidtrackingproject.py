import pandas as pd

from states_dict import states_dict

def get_covid_tracking_data():


    # gets testing (and other!) data from Covid Tracking Project

    # Returns: dictionary of dataframes, key/value indicating different data sources aggregated by the Project as below

    # states_current    : current state data
    # states_historical : historical state wise data, updated 4pm ET
    # us_current        : current us data
    # us_historical     : historical us data, updated 4pm ET
    # states_info       : information sources for state wise data


    # states_current:

    covid_tracking_api_url = 'https://covidtracking.com/api/'


    covid_tracking_urls = dict(states_current=covid_tracking_api_url + 'states.csv',
                               states_historical=covid_tracking_api_url + 'states/daily.csv',
                               us_current=covid_tracking_api_url + 'us.csv',
                               us_historical=covid_tracking_api_url + 'us/daily.csv',
                               states_info=covid_tracking_api_url + 'states/info.csv')

    covid_tracking_dfs = dict()


    for covid_tracking_datatype in covid_tracking_urls :

        covid_tracking_dfs[covid_tracking_datatype] = pd.read_csv(covid_tracking_urls[covid_tracking_datatype])
        if "state" in covid_tracking_dfs[covid_tracking_datatype]: covid_tracking_dfs[covid_tracking_datatype].state = covid_tracking_dfs[covid_tracking_datatype].state.map(states_dict)
        if "date" in covid_tracking_dfs[covid_tracking_datatype]: covid_tracking_dfs[covid_tracking_datatype].date = pd.to_datetime(covid_tracking_dfs[covid_tracking_datatype].date, format ='%Y%m%d').dt.strftime('%m/%d/%y')
    return covid_tracking_dfs





