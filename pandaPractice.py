import pandas as pd

# Link to the csv source and variable meanings 
# http://inalitic.com/datasets/nhl%20player%20data.html

# Hockey data practice
hockey_data =pd.read_csv("skater_stats.csv",encoding = "ISO-8859-1",low_memory=False,
	dtype={'GP': int})
#delete unecessary column
del hockey_data['Unnamed: 0']

#---- prepping all colmns to be same data type --

# some values in 'G' and 'A' are problematic such that they are special charecters, convert those to NaN
hockey_data['G'] = pd.to_numeric(hockey_data['G'], errors='coerce') # fixes "invalid literal for int() with base 10: ' -   '
hockey_data['A'] = pd.to_numeric(hockey_data['A'], errors='coerce') # fixes "invalid literal for int() with base 10: ' -   '
hockey_data['PTS'] = pd.to_numeric(hockey_data['PTS'], errors='coerce') # fixes "invalid literal for int() with base 10: ' -   '
hockey_data['S'] = pd.to_numeric(hockey_data['S'], errors='coerce') # fixes "invalid literal for int() with base 10: ' -   '

# now fill in empty slots
hockey_data = hockey_data.fillna(0) # fixes "Cannot convert non-finite values (NA or inf) to integer"

# finally convert to int 
#if all values are numbers , this works but first fill in empty spaces ^^
hockey_data['G']=hockey_data['G'].astype(int)
hockey_data['A']=hockey_data['A'].astype(int)
hockey_data['PTS']=hockey_data['PTS'].astype(int)
hockey_data['S']=hockey_data['S'].astype(int)

#prints first 3 rows
print(hockey_data.head(3))
print('\n')

#print last 3  rows
print(hockey_data.tail(3))
print('\n')

#import excel file
#hockey_data=pd.read_excel("hohecky.xlsx")
#print(data_xlsx.tail(3))


#import txt file
#hockey_data= pd.read_csv("skater_stats.csv.txt",delimiter='\t')
#print(data_tabSep.head(4))


#print colums
#will print all rows of specific column
print(hockey_data[['Season','Player','Tm','G']])
print('\n')

#will print all details of specific row given index num , 0=first row ..
#print(hockey_data.iloc[1])


#or multiple rows ( will get rows 0 ,1 ,2)
#print(hockey_data.iloc[0:3])

#get row 2 , column column 1 .. prints 1 attribute
#print(hockey_data.iloc[0,1])
#print('\n')

#will print all rows but only  Name column
#index =0
#for index,row in hockey_data.iterrows():
	#print(index,row['Player'])

#print('\n')

#get mean , min, std , max etc..
#print(hockey_data.describe())


# sort by team asc and Goals Decs
print(hockey_data.sort_values(['Tm','G'],ascending=[1,0]))
print('\n')

# add columns G+A
hockey_data['Total']= hockey_data['G'] + hockey_data['A']
print(hockey_data[['Player','Total']])
print('\n')

#drop column G+ATotal
hockey_data = hockey_data.drop(columns=['Total'])

# if all values were numbers , this would work
#hockey_data['G']=hockey_data['G'].astype(int)



# second adding method
#" : " means all rows
hockey_data['Total'] =hockey_data.iloc[:,5:8].sum(axis=1)
print(hockey_data.head())

print('\n')



# Get a Series object containing the data type objects of each column of Dataframe.
# Index of series is column name.
dataTypeHockey = hockey_data.dtypes
#print('Data type of each column of Dataframe :')
print(dataTypeHockey)

#print(hockey_data.head())

# take data from dataframe and create a new file with modified attributes
#hockey_data.to_csv('new_hockey_player_stats.csv')
# if we want to remove column indexes , column 0
#hockey_data.to_csv('new_hockey_player_stats.csv', index = False)
#to excel
#hockey_data.to_excel('new_hockey_player_stats.xlsx')

#-- Filtering Data --
# filter By Anaheim team AND Season 2007.. can use OR
#print(hockey_data.loc[(hockey_data['Tm'] == ' ANA ') & (hockey_data['Season'] == 2007)])
print('\n')

# By team , Goals greater than 30
#print(hockey_data.loc[(hockey_data['Tm'] == ' ANA ') & (hockey_data['G'] > 30)])
print('\n')

# can save new dataframe with out modifing previous dataframe
# good for check point ..saving work

# new_hockey_data = hockey_data.reset_index(drop=True) # optional reseting index numbers
new_hockey_data = hockey_data.loc[(hockey_data['Tm'] == ' ANA ') & (hockey_data['G'] > 30)]
#new_hockey_data.to_csv('new_hockey_player_stats.csv')

# import regular expression
import re
#using regular expression get rows where PLayer column equals Kariya or Selanne
#print(hockey_data.loc[hockey_data['Player'].str.contains(' Kariya| Selanne',regex =True)])
print('\n')

# flags = re.I mean Caplztn does not matter , * is many or More ,^ is start of line ..otherwise anywhere in name
#print(hockey_data.loc[hockey_data['Player'].str.contains('^re[a-z]*',flags = re.I,regex =True)])


# -- conditional changes --

# Change all instances of "ANA" to "DUC" within Tm column
#hockey_data.loc[hockey_data['Tm'] == ' ANA ' , 'Tm'] = 'DUC'
#print(hockey_data.loc[(hockey_data['Tm'] == 'DUC')])

# revert back to "ANA"
#hockey_data.loc[hockey_data['Tm'] == 'DUC' , 'Tm'] = ' ANA '
#print(hockey_data.loc[(hockey_data['Tm'] == ' ANA ')])

# Where Tm equals "ANA" , set Total to 99
# cannot revert to original Total data ..use checkpoint
hockey_data.loc[hockey_data['Tm'] == ' ANA ' , 'Total'] = 99
#print(hockey_data.loc[(hockey_data['Tm'] == ' ANA ')])


# create new column to hold if more than 50 goals a season was True or False
hockey_data['MoreThan50'] = False # initialize False
#print(hockey_data.head())

hockey_data.loc[hockey_data['G'] > 50, 'MoreThan50'] = True

# Default value of display.max_rows is 10 i.e. at max 10 rows will be printed.
# Set it None to display all rows in the dataframe
pd.set_option('display.max_rows', 10)

# create a new Dataframe of Players with 50 or more goals
players_w_50_goals =hockey_data.loc[(hockey_data['MoreThan50'] == True)]

# display all players who scored more than 50 Goals a season 
# WILL only sort for display , dataframe not changed
#print(players_w_50_goals.sort_values('G',ascending =False))

#create new csv file with new data
players_w_50_goals=players_w_50_goals.drop(columns=['Total']) #drop this colum
players_w_50_goals= players_w_50_goals.sort_values('G',ascending =False) # sort by Desc
# create CSV file and remove indexing
#players_w_50_goals.to_csv('50_Or_More_Goals_Ssn.csv', index = False)


# -- Aggregate Statistics ..Groupby --

# group by Player column, get mean of columns and sort by Games played Desc
# print(hockey_data.groupby(['Player']).mean().sort_values('GP',ascending=False))

# data with the sum of Goals,Assts,TotalPoint per season,and shots taken per season
# Sorted by most Total Points earned 
Teams_Basic_stats=hockey_data.groupby(['Tm']).sum()[['G','A','S','PTS']]
Teams_Basic_stats= Teams_Basic_stats.sort_values('PTS',ascending =False) # sort by Desc
Teams_Basic_stats.to_csv('Teams_Basic_stats.csv')

print(Teams_Basic_stats)



