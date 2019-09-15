**Hypothesis:** University towns have their mean housing prices less effected by recessions. 
Run a t-test to compare the ratio of the mean 
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
    
    
    
#### Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

The following cleaning needs to be done by function below:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"] 
    
    def get_list_of_university_towns():

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
    
The following is done by function below:
'''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    
    def get_recession_start():
    
    df=pd.read_excel('gdplev.xls',header=None)
    df=df[8:]
    df.columns=['Year', 'AnnualGDPCur', 'AnnualGDPChain','dr1', 'YearQuater','QuaterGDPCur', 'QuaterGDPChain','dr2']
    df=df.reset_index()
    df.drop(['index','dr1','dr2'],axis=1,inplace=True)
    df['1qdiff'] = df['QuaterGDPCur'].shift(1)
    df['1qdiffres'] = df['QuaterGDPCur']-df['1qdiff']
    #recession=[]
    for i in (df.index[1:-2]):
        if ((df['1qdiffres'].ix[i+2] < 0)& (df['1qdiffres'].ix[i+1] < 0)&(df['1qdiffres'].ix[i-1] > 0)& (df['1qdiffres'].ix[i] > 0)):
               recessionStart=(df['YearQuater'].ix[i])#recession.append(df['YearQuater'].ix[i])
    
    return recessionStart


The following is done by function below: 
'''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    
    def get_recession_bottom():
  
    df=pd.read_excel('gdplev.xls',header=None)
    df=df[8:]
    df.columns=['Year', 'AnnualGDPCur', 'AnnualGDPChain','dr1', 'YearQuater','QuaterGDPCur', 'QuaterGDPChain','dr2']
    df=df.reset_index()
    df.drop(['index','dr1','dr2'],axis=1,inplace=True)
    df['1qdiff'] = df['QuaterGDPCur'].shift(1)
    df['1qdiffres'] = df['QuaterGDPCur']-df['1qdiff']
    recession=[]
    rec = df[df['YearQuater']>=get_recession_start()].index#.astype('int')
    for i in (rec[:-2]):
        if ((df['1qdiffres'].ix[i+2] < 0)& (df['1qdiffres'].ix[i+1] < 0)):
               recession.append(df['YearQuater'].ix[i])
               recession.append(df['YearQuater'].ix[i+1])
               recession.append(df['YearQuater'].ix[i+2])
            
    lowGDP = df['YearQuater'][df['QuaterGDPCur'].where(df['YearQuater'].isin(recession)).idxmin()]
    return lowGDP
    
    
The following is done by the function below:
'''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    '''
    
    import time as tm
    import datetime  as dt
    def convert_housing_data_to_quarters():
    data = pd.read_csv('City_Zhvi_AllHomes.csv')
    lst=['RegionID', 'RegionName', 'State', 'Metro', 'CountyName', 'SizeRank','1996-04', '1996-05', '1996-06', '1996-07','1996-08',          '1996-09', '1996-10', '1996-11', '1996-12', '1997-01', '1997-02', '1997-03', '1997-04', '1997-05', '1997-06', '1997-07','1997-08',      '1997-09', '1997-10', '1997-11','1997-12', '1998-01', '1998-02', '1998-03','1998-04', '1998-05', '1998-06', '1998-07','1998-08',         '1998-09', '1998-10', '1998-11','1998-12', '1999-01', '1999-02', '1999-03','1999-04', '1999-05', '1999-06', '1999-07','1999-08',         '1999-09', '1999-10', '1999-11','1999-12']
    opn= data.drop(lst,axis=1)
 
    Xopn=pd.DataFrame(data[['State', 'RegionName']])
    for year in range(2000,2016):
        Xopn[str(year)+'q1'] = opn[[str(year)+'-01',str(year)+'-02',str(year)+'-03']].mean(axis=1)
        Xopn[str(year)+'q2'] = opn[[str(year)+'-04',str(year)+'-05',str(year)+'-06']].mean(axis=1)
        Xopn[str(year)+'q3'] = opn[[str(year)+'-07',str(year)+'-08',str(year)+'-09']].mean(axis=1)
        Xopn[str(year)+'q4'] = opn[[str(year)+'-10',str(year)+'-11',str(year)+'-12']].mean(axis=1)
    year = 2016    
    Xopn[str(year)+'q1'] = opn[[str(year)+'-01',str(year)+'-02',str(year)+'-03']].mean(axis=1)
    Xopn[str(year)+'q2'] = opn[[str(year)+'-04',str(year)+'-05',str(year)+'-06']].mean(axis=1)
    Xopn[str(year)+'q3'] = opn[[str(year)+'-07',str(year)+'-08']].mean(axis=1)
    
    Xopn.replace({"State": states},inplace=True)
    Xopn.set_index(['State','RegionName'],drop=True,inplace=True)
    
    return Xopn 
    
    
    The following is done by function below:
     '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    from scipy import stats
    def run_ttest():
   
    recession_bottom=get_recession_bottom()
    recession_start=get_recession_start()
    university_towns=get_list_of_university_towns()
    housing_data=convert_housing_data_to_quarters().dropna()
    ndata = housing_data.ix[:,recession_start:recession_bottom ]
    ndata=ndata.reset_index()
    university_towns=university_towns.reset_index().drop('index',axis=1)
    unitowndata= ndata[ndata['RegionName'].isin(university_towns['RegionName'])] 
    notunitowndata= ndata[~ndata['RegionName'].isin(university_towns['RegionName'])]
    unitowndata['Ratio']= ((unitowndata[recession_start]- unitowndata[recession_bottom])/unitowndata[recession_start]).dropna()
    notunitowndata['Ratio']= ((notunitowndata[recession_start]- notunitowndata[recession_bottom])/ notunitowndata[recession_start]).dropna()
    print(len(unitowndata))
    print(len(notunitowndata))
    stat,pval=(stats.ttest_ind(unitowndata['Ratio'], notunitowndata['Ratio']))
    if pval <0.01:
        different = True
        better= "university town"
    else:
        different = False
        better= "non-university town"
    return  (different,pval,better)


The Final RESULT:

(True, 0.00076409873531842394, 'university town')
