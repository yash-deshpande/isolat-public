import json
import pandas as pd
import time
import sys
from states_dict import states_dict

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3
    from urllib import urlopen

def get_kinsa_data(input_states_list = None):
    """Returns a dataframe of Kinsa data """
    # Input:   
    # (optional) input_states_list: list of state abbreviations to pull data from, e.g. ['CA'], ['CA', 'VT']...
    
    # Output if not None:
    # kinsa_df: Dataframe of kinsa data. Check kinsa_df.head() and following link for more info
    # https://content.kinsahealth.com/covid-detection-technical-approach for methodology
    
    if input_states_list is None: # default, get all states
        states_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    else: # check that input states list is okay
        full_states_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        
        for potential_state in input_states_list:
            if potential_state not in full_states_list:
                print('Input list contains unrecognized state, returning None')
                return None
        # input state list is sublist of full states list
        states_list = input_states_list
                
    
    kinsa_path = 'https://static.kinsahealth.com/' 
    # initialize empty list of statewise dataframes to concatenate later
    states_data = []
    # for each state pull the data and append to states_data
    for state in states_list:
        
        #create path to pull from, e.g. AL is https://static.kinsahealth.com/AL_data.json
        state_path = kinsa_path + state + '_data.json'
        #pull the data
        try:
            response = urlopen(state_path)
            state_data = json.loads(response.read())
            # construct a dataframe from read data
            state_df = pd.DataFrame(state_data['data'], columns = state_data['columns'])
            # append this to states_data
            states_data.append(state_df)
        except:
            print ('Could not download data from url ' + state_path)
        
        time.sleep(0.5)

    # concatenate list to form single dataframe
    kinsa_df = pd.concat(states_data, axis=0)
    if "state" in kinsa_df: kinsa_df.state = kinsa_df.state.map(states_dict)
    if "date" in kinsa_df: kinsa_df.date = pd.to_datetime(kinsa_df.date, format ='%Y-%m-%d').dt.strftime('%m/%d/%y')



    return kinsa_df


