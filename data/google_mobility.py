import pandas as pd


def get_google_mobility_data():
    """ returns dataframe of Google mobility data"""
    
    # mobility path
    mobility_path = "https://raw.githubusercontent.com/vitorbaptista/google-covid19-mobility-reports/master/data/processed/mobility_reports.csv"
    
    # import from path if possible, else return error message
    try:
        raw_google_mobility_df = pd.read_csv(mobility_path)
    except:
        print('Cannot read path '+ mobility_path+ ', returning None')    
        return None
    
    # rename and reformat date column
    google_mobility_df = raw_google_mobility_df.rename(columns = {'updated_at': 'date'})
    
    if "date" in google_mobility_df:
        google_mobility_df.date = pd.to_datetime(google_mobility_df.date, format ='%Y-%m-%d').dt.strftime('%m/%d/%y')
        
  

    return google_mobility_df


def get_google_mobility_ts(region = 'global'):
    """ returns a dictionary of dataframes of Google mobility data
    region: can either be global or US
    
    """
    if region == 'global':
        mobility_path = "https://covid19-analysis.netlify.app/mobility/world.csv"
    elif region == "US":
        mobility_path= "https://covid19-analysis.netlify.app/mobility/US.csv"
    else:   
        raise ValueError  ('invalide region, should be : US or global\n')

    df = pd.read_csv(mobility_path)
    
    if "date" in df:
        df.date = pd.to_datetime(df.date, format ='%Y-%m-%d').dt.strftime('%m/%d/%y')

    return df