Energy Indicators.xls contains a list of indicators of energy supply and renewable electricity production from the United Nations for
the year 2013, and should be put into a DataFrame with the variable name of energy.

Rename the following list of countries (for use in later questions):
"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,e.g.
'Bolivia (Plurinational State of)' should be 'Bolivia',
'Switzerland17' should be 'Switzerland'.

Next,the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank.
Rename the following list of countries:
"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"

Finally, the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology is in the file scimagojr-3.xlsx, 
which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

Joining the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Using only the last 10 
years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).


    import pandas as pd
    def answer_one():
    
    missing_values = ["n/a", "na", "--","..."]
    data=pd.read_excel('Energy Indicators.xls', na_values=missing_values, skiprows=17,skip_footer= 38)
    energy = data#[19:243]
    energy.drop(energy.columns[[0,1]], axis = 1, inplace = True)
    energy.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[ 'Energy Supply']=energy[ 'Energy Supply']* 1000000
   
    energy['Country']= energy['Country'].str.replace("\d+",'').map(lambda x: x.split(" (")).str[0].map(lambda x: x.split("(")).str[0]
    energy['Country'][energy['Country']=="Republic of Korea"] = "South Korea"
    energy['Country'][energy['Country']=="United States of America"] = "United States"
    energy['Country'][energy['Country']=="United Kingdom of Great Britain and Northern Ireland"] = "United Kingdom"
    energy['Country'][energy['Country']=="China, Hong Kong Special Administrative Region"] = "Hong Kong"

    data2=pd.read_csv('world_bank.csv', na_values=missing_values,skiprows=4)

    GDP=data2
    GDP.columns=['Country','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    GDP = GDP.drop(['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005'], axis=1)
    GDP['Country'][GDP['Country']=="Korea, Rep."] = "South Korea"
    GDP['Country'][GDP['Country']=="Iran, Islamic Rep."] = "Iran"
    GDP['Country'][GDP['Country']=="Hong Kong SAR, China"] = "Hong Kong"
    
    
    ScimEn=pd.read_excel('scimagojr-3.xlsx',na_values=missing_values)
    
    GDP.drop(['Country Code','Indicator Name','Indicator Code'], axis=1, inplace=True)
    dfbase=pd.merge(pd.merge(ScimEn,energy, how='inner', left_on='Country', right_on='Country'), GDP,how='inner', left_on='Country', right_on='Country')
    
    lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    dfbase=dfbase.loc[dfbase['Rank'].isin(lst)]
    dfbase.set_index( 'Country',drop=True,inplace=True)
    dfbase.sort_values(by=['Rank'],inplace=True)
    typechngint =['Rank','Documents','Citable documents','Citations','Self-citations','H index',]
    dfbase[typechngint] = dfbase[typechngint].astype('float')
    typechngfloat = ['Energy Supply','Energy Supply per Capita', '% Renewable']
    energy[typechngfloat] = energy[typechngfloat].astype('float')

    return (dfbase)
    
    
To find  the mean Energy Supply per Capita:
   
    import numpy as np
    def answer_two():
    Top15 = answer_one()
    return  Top15['Energy Supply per Capita'].mean()


Write  a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's 
% Renewable value is below the median.

    def answer_three():
    Top15 = answer_one()
    Top15['HighRenew'] = Top15['% Renewable'] >= Top15['% Renewable'].median()
    return Top15['HighRenew']*1
    
    
To find the  estimation of number of citable documents per person and What is the correlation between the number of citable documents
per capita and the energy supply per capita?

    def answer_four():
    Top15 = answer_one()
    Top15['PopEst']= (Top15['Energy Supply'] / Top15['Energy Supply per Capita'])#
    Top15['CitationperCapita']= Top15['Citations']/Top15['PopEst']
    
    return Top15['CitationperCapita'].corr(Top15['Energy Supply per Capita'])

   
 The Final RESULT:
 0.66682
    
    
