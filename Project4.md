Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean 
price of houses in university towns the quarter before the recession starts compared to the recession bottom. 
(price_ratio=quarter_before_recession/recession_bottom)

Definitions:

    - A quarter is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, 
    Q4 is October through December.
    - A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    - A recession bottom is the quarter within a recession which had the lowest GDP.
    - A university town is a city which has a high percentage of university students compared to the total population of the city.

The following data files are available for this assignment:

    - From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes at a city 
    level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
    - From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted into the file university_towns.txt.
    - From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars 
    (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at GDP data
    from the first quarter of 2000 onward.
    
    
    
# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    
def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"] 
    df = pd.read_table('university_towns.txt',sep="\n",names=['col'])
    st=''
    dfout=pd.DataFrame( [],columns=["State", "RegionName"] )
    df['col']=df['col'].map(lambda x:x.split('[')).str[0] #.map(lambda x:x.split('\n')).str[0]
    sorted(states.items(), key = lambda x : x[1])
    idx = df['col'].isin(states.values())
    for i,val in idx.items():
        if (val):
            st=df['col'].ix[i]
        else:
            dfout = dfout.append({'State' : st , 'RegionName' : df['col'].ix[i]} , ignore_index=True)
    dfout['State']=dfout['State'].map(lambda x:x.split('[')).str[0]
    dfout['RegionName']=dfout['RegionName'].map(lambda x:x.split(' (')).str[0]
    return dfout
    
