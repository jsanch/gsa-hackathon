# Joins DOT flight data to the provided GSA flight data

import pandas as pd 
import datetime

# Dot quarterly fares. 
dot = pd.read_csv("2011_2014_Table1a.csv")

# Filtered dataset with only ~50K out of the 60K given at the hackathon. 
# Only looking at oneway, and direct standard rountrip flights
directandround = pd.read_csv("oneway_and_roundtrip.csv") 

def get_quarter_from_date(date):
	d = datetime.datetime.strptime(date, "%m/%d/%Y")
	quarter = (d.month-1)//3 + 1
	return str(d.year) +'.'+ str(quarter)



#Creates a lookup dictionary
le_dict = {}
for dot_i, dot_row in dot.iterrows():
	le_dict[str(dot_row['Year']) + '.' + str(dot_row['quarter']) + '.' + str(dot_row['airport_1']) + '.' +  str(dot_row['airport_2'])] = dot_row
	le_dict[str(dot_row['Year']) + '.' + str(dot_row['quarter']) + '.' + str(dot_row['airport_2']) + '.' +  str(dot_row['airport_1'])] = dot_row


#adds DOT fares to original dataset
for directandround_i, directandround_row in directandround.iterrows():
	code =  get_quarter_from_date(directandround_row['Trip Departure Date'])+'.'+directandround_row['Origin Airport Code']+'.'+directandround_row['Destination Airport Code']
	if code in le_dict:
		print le_dict[code]
		directandround.ix[directandround_i, 'dot_fare']  = le_dict[code]['fare']
		directandround.ix[directandround_i, 'dot_fare_low']  = le_dict[code]['fare_low']



