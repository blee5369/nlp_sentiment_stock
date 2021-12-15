import pandas as pd

from mordecai import Geoparser
geo = Geoparser()
countries = []
confidence = []
news = pd.read_csv('abcnews-date-text.csv')
count = 1 
for headline in news['headline_text']:
    # Intermediate printing and writing to disk every 50k records
    if count % 50000 ==0: 
        print('50k done')
        part = news[:count-1]
        part['country_predicted'] = countries
        part['country_conf'] = confidence
        part.to_csv(f'abcnews-date-text-mordecai_part_{count}.csv')
    # Catch keras Neural net build failures
    try:
        response = geo.geoparse(headline)
        # if mordecai found any countries 
        if len(response) > 0:
            countries.append(response[0]['country_predicted'])
            confidence.append(response[0]['country_conf'])
        else:
            countries.append(None)
            confidence.append(None)
    except ValueError: 
        countries.append(None)
        confidence.append(None)
    count+=1

# Write total file to disk 
news['country_predicted'] = countries
news['country_conf'] = confidence

news.to_csv('abcnews-date-text-mordecai.csv')