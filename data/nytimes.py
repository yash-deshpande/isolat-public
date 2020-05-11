import pandas as pd


def get_nyt_data():
    # collect latest data from nytimes source
    # Returns:
    #(state_df, county_df) tuple of dataframes containing state- and county-wise data from NYtimes.

    # URLs of NYTimes data
    URL_State = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    URL_County = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    
    dtype_dict = {u'date'   : 'str', 
                      u'county' : 'str', 
                      u'state'  : 'str', 
                      u'fips'   : 'str',
                      u'cases'  : 'int32', 
                      u'deaths' : 'int32'}
    
    
    state_df = pd.read_csv(URL_State, dtype = dtype_dict)
    county_df = pd.read_csv(URL_County, dtype = dtype_dict)
    # unify date format
    state_df.loc[:,'date'] = pd.to_datetime(state_df['date']).dt.strftime('%m/%d/%y')
    county_df.loc[:,'date'] = pd.to_datetime(county_df['date']).dt.strftime('%m/%d/%y')
    # convert cases, deaths 
    
    return state_df, county_df


def convert_state_df_to_ts(df, quantity, naval=None):
    """Converts a state dataframe to a time series of quantity per state"""
    #     # df  : input dataframe
    #     # quantity :  column that you want to aggregate for time series
    #     # naval: fill na's with this value, defaults to None which means no fill 
    try:
        dates = df.loc[:, 'date'].unique()
    except KeyError:
        print('Input dataframe has does not have "date" column, returning None ')
        return None
    
    try:
        df.loc[:, quantity]
    except KeyError:
        print('Input dataframe does not have a ' + quantity + ' column, returning None')
        return None
    
    # dataframe now has date, quantity columns
    
    states_time_series_list= [pd.Series(pd.Series(frame[quantity].values, index=frame['date'], name=state),
                                      index=dates)
                            for state, frame in df.groupby('state')]
    

    new_df = pd.concat(states_time_series_list, axis=1)
    new_df = new_df.transpose()

    # fill na values with naval if given
    if naval is not None:
        new_df = new_df.fillna(naval)

    new_df.insert(0, 'state', new_df.index)

    return new_df


def convert_county_df_to_ts(df, quantity, naval=None):
    """Converts a county, state dataframe to a time series equivalent"""
    #     # df  : input dataframe
    #     # quantity :  'cases' or 'deaths' depending on which quantity you want to aggregate for time series
    #     # naval: fill na's with this value, defaults to None or no filling

    try: # check if df has dates
        dates = df.loc[:, 'date'].unique()
    except KeyError:
        print('Input dataframe has does not have a "date" column, returning None')
        return None
    
    try: # check if df has required column
        df.loc[:, quantity]
    except KeyError:
        print('Input dataframe does not have a ' + quantity + ' column, returning None')
        return None
    # create list of Series: each Series is a time series
    counties_time_series_list = [pd.Series(frame[quantity].values, 
                                           index=frame['date'], 
                                           name=county_state_pair)
                                 for county_state_pair, frame in df.groupby(['state', 'county'])]
    # remove duplace indices if they exist
    counties_time_series_list = [ series_[~series_.index.duplicated()] for series_ in counties_time_series_list ]
    # reindex to all available unique, fill with nans 
    counties_time_series_list = [series_.reindex(index=dates) for series_ in counties_time_series_list]


    county_column = [county_state_pair[1] for county_state_pair, frame in df.groupby(['state', 'county'])]
    state_column = [county_state_pair[0] for county_state_pair, frame in df.groupby(['state', 'county'])]

    new_df = pd.concat(counties_time_series_list, axis=1).transpose()

    # fill na values with naval if given
    if naval is not None:
        new_df = new_df.fillna(naval)

    new_df.insert(0, 'state', state_column)
    new_df.insert(0, 'county', county_column)

    return new_df
