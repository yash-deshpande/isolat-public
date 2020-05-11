import pandas as pd

def get_india_data():
    """ returns dataframe of india covid data"""
    
    
    india_path = 'https://prsindia.org/covid-19/cases/download'
    # do try except here:
    try:
        raw_india_df = pd.read_csv(india_path)
    except:
        print('Cannot read path '+ india_path+ ', returning None')
        return None
    
    #drop excess column 
    india_df = raw_india_df.drop('S. No.', axis=1)
    # rename and reformat date column
    india_df = india_df.rename(columns = {'Date': 'date'})
    if "date" in india_df:
        india_df.date = pd.to_datetime(india_df.date, format ='%d/%m/%Y').dt.strftime('%m/%d/%y')
        
    # drop world rows
    india_df = india_df.loc[india_df.Region != u'World', :]

    return india_df