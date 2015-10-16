# Join on
# 	Date 
# 	Origin
# 	Destination


get_quarter_from_date(directandround_row['Trip Departure Date'])  ==  str(dot['Year'])+ str(dot['quarter'])
directandround_row['Origin Airport Code'] == dot_row['airport_1'] 
directandround_row['Destination Airport Code'] == dot_row['airport_2']


for index,row in dot.iterrows():
    print str(row['Year']) 



def get_quarter_from_date(date):
	d = datetime.datetime.strptime(date, "%m/%d/%Y")
	quarter = (d.month-1)//3 + 1
	return str(d.year) +'.'+ str(quarter)



for directandround_i, directandround_row in directandround.iterrows():
	print "index", str(directandround_i)
	for dot_i, dot_row in dot.iterrows():
		if get_quarter_from_date(directandround_row['Trip Departure Date']) == str(dot_row['Year']) + '.' + str(dot_row['quarter']):
			if ( (directandround_row['Origin Airport Code'] == dot_row['airport_1']) and (directandround_row['Destination Airport Code'] == dot_row['airport_2']) ) or ( (directandround_row['Origin Airport Code'] == dot_row['airport_2']) and (directandround_row['Destination Airport Code'] == dot_row['airport_1']) ) :
					directandround_row['dot_fare']  = dot_row['fare']
					directandround_row['dot_fare_low']  = dot_row['fare_low']
					print "Routing: ", directandround_row['Routing'], "GSA Fare: ", directandround_row["Total Amount"], "DOT Fare: ",directandround_row['dot_fare']



le_dict = {}
for dot_i, dot_row in dot.iterrows():
	le_dict[str(dot_row['Year']) + '.' + str(dot_row['quarter']) + '.' + str(dot_row['airport_1']) + '.' +  str(dot_row['airport_2'])] = dot_row
	le_dict[str(dot_row['Year']) + '.' + str(dot_row['quarter']) + '.' + str(dot_row['airport_2']) + '.' +  str(dot_row['airport_1'])] = dot_row



for directandround_i, directandround_row in directandround.iterrows():
	code =  get_quarter_from_date(directandround_row['Trip Departure Date'])+'.'+directandround_row['Origin Airport Code']+'.'+directandround_row['Destination Airport Code']
	if code in le_dict:
		print le_dict[code]
		directandround_row['dot_fare']  = le_dict[code]['fare']
		directandround_row['dot_fare_low']  = dle_dict[code]['fare_low']



