# CoVid-19
## Covid 19 IDSS Repo

### This is a public clone of the IDSS, MIT CoVid-19 working group(Isolat) repository

Disclaimer:
Isolat’s purpose is to improve access to various publicly available data sources for analysis. We do not assume responsibility for the data accessed using our tools, nor for use of data accessed through our tools. Before making use of data accessed using our tools, please check with the original source for terms and conditions of use. Please remember to be ‘nice’ while using our tools for programmatic access of public data sources.    



## Datasets:
Datasets from the following sources are available.  
Refer to example.py for instructions on how to load the data.
To install intervention data, you will need to install several packages. Please run
 
`pip install -r requirements.txt` 


 1. New York Times (nytimes.py):
Daily number of cases/deaths in US states and counties.

 2. John Hopkins University (jhu.py).
Daily number of cases/deaths/and recovered cases globally and in the US.

 3. Covid Tracking Project (covidtrackingproject.py):
which has the following datasets:

    -  states_current    : current state data
    -  states_historical : historical state wise data, updated 4pm ET
    -  us_current        : current US data
    -  us_historical     : historical US data, updated 4pm ET
    -  states_info       : information sources for state wise data


 4. The Humanitarian Data Exchange (hdx.py):
Timestamped interventions data on global (countries) level.
Sample rows:  

|    |   id | country     | iso   | admin_level_name   |   pcode | region   | category               | measure                                            | targeted_pop_group   |   comments |   non_compliance | date_implemented   | source             | source_type   | link                                                                                                                       | entry_date   |   alternative_source |
|---:|-----:|:------------|:------|:-------------------|--------:|:---------|:-----------------------|:---------------------------------------------------|:---------------------|-----------:|-----------------:|:-------------------|:-------------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------|:-------------|---------------------:|
|  0 |    1 | Afghanistan | AFG   | nan                |     nan | Asia     | Public health measures | Health screenings in airports and border crossings | No                   |        nan |              nan | 02/12/20           | Ministry of Health | Government    | https://moph.gov.af/en/moph-held-emergency-meeting-international-health-partners-fight-against-spread-and-control-covid-19 | 03/14/20     |                  nan |
|  1 |    2 | Afghanistan | AFG   | Kabul              |     nan | Asia     | Public health measures | Introduction of quarantine policies                | No                   |        nan |              nan | 02/12/20           | Ministry of Health | Government    | https://moph.gov.af/en/moph-held-emergency-meeting-international-health-partners-fight-against-spread-and-control-covid-19 | 03/14/20     |                  nan |


 5. NGA (nga.py):
Interventions data on US states level. The data shows whether a certain intervention measure is taken in each state. 


 6. Unacast (unacast.py):
Social distancing scores for US states and counties.
Sample rows:

|    | date     | county_name   |   county_fips | vistation_grade   | travel_distance_grade   | total_grade   |
|---:|:---------|:--------------|--------------:|:------------------|:------------------------|:--------------|
|  0 | 04/03/20 | Tama County   |         19171 |                   | D                       | D             |
|  1 | 04/02/20 | Tama County   |         19171 |                   | D                       | D 


 7. beoutbreakprepared (beoutbreakprepared.py):
Detailed data for individual cases inclusing demographics, location,  province, and country.
Sample rows: 


|    | ID     | age   | sex    | city             | province   | country       |   wuhan(0)_not_wuhan(1) |   latitude |   longitude | geo_resolution   |   date_onset_symptoms |   date_admission_hospital | date_confirmation   |   symptoms |   lives_in_Wuhan |   travel_history_dates |   travel_history_location |   reported_market_exposure |   additional_information |   chronic_disease_binary |   chronic_disease | source                                           |   sequence_available |   outcome |   date_death_or_discharge |   notes_for_discussion |   location |   admin3 | admin2           | admin1     | country_new   |   admin_id |   data_moderator_initials |   travel_history_binary |
|---:|:-------|:------|:-------|:-----------------|:-----------|:--------------|------------------------:|-----------:|------------:|:-----------------|----------------------:|--------------------------:|:--------------------|-----------:|-----------------:|-----------------------:|--------------------------:|---------------------------:|-------------------------:|-------------------------:|------------------:|:-------------------------------------------------|---------------------:|----------:|--------------------------:|-----------------------:|-----------:|---------:|:-----------------|:-----------|:--------------|-----------:|--------------------------:|------------------------:|
|  0 | 000-1- | 30-39 | female | Snohomish County | Washington | United States |                       1 |    48.0482 |   -121.696  | admin2           |                   nan |                       nan | 11.03.2020          |        nan |              nan |                    nan |                       nan |                        nan |                      nan |                      nan |               nan | https://www.snohd.org/484/Novel-Coronavirus-2019 |                  nan |       nan |                       nan |                    nan |        nan |      nan | Snohomish County | Washington | United States |       2988 |                       nan |                     nan |
|  1 | 000-1- | nan   | nan    | nan              | Khuzestan  | Iran          |                       1 |    31.4962 |     48.9673 | admin1           |                   nan |                       nan | 01.03.2020          |        nan |              nan |                    nan |                       nan |                        nan |                      nan |                      nan |               nan | Iran Ministry of Health                          |                  nan |       nan |                       nan |                    nan |        nan |      nan | nan              | Khuzestan  | Iran          |         15 |                       nan |                     nan |





 8. Kinsa Health (kinsa.py)
Data for county-wise illness incidence and forecast reported by [Kinsa Health](https://www.kinsahealth.co/) 
    
 9. Google Mobility data (google_mobility.py)
Google Mobility scores (global and US level) for different sectors. Taken from Google Covid-19 mobility reports. [Source]( https://covid19-analysis.netlify.app)
