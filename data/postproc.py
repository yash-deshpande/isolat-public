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
    counties_time_series_list = [pd.Series(pd.Series(frame[quantity].values, index=frame['date'], name=county_state_pair),
                                        index=dates)
                              for county_state_pair, frame in df.groupby(['county', 'state'])]

    county_column = [county_state_pair[0] for county_state_pair, frame in df.groupby(['county', 'state'])]
    state_column = [county_state_pair[1] for county_state_pair, frame in df.groupby(['county', 'state'])]

    new_df = pd.concat(counties_time_series_list, axis=1).transpose()

    # fill na values with naval if given
    if naval is not None:
        new_df = new_df.fillna(naval)

    new_df.insert(0, 'state', state_column)
    new_df.insert(0, 'county', county_column)

    return new_df