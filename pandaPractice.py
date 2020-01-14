import pandas as pd


#pokemon data practice
data=pd.read_csv("pokemon_data.csv")
print(data.head(3))
print('\n')

data_xlsx=pd.read_excel("pokemon_data.xlsx")
#print(data_xlsx.tail(3))
print('\n')

data_tabSep= pd.read_csv("pokemon_data.txt",delimiter='\t')
#print(data_tabSep.head(4))
print('\n')

#print colums
#will print all
#print(data[['Name','HP','Speed']])
print('\n')

#will print all details of index 0 only
#print(data.iloc[0])
print('\n')

#or multiple rows ( will get rows 0 ,1 ,2)
#print(data.iloc[0:3])
print('\n')

#get row 2 , column index 1
#print(data.iloc[2,1])
print('\n')

#will print all rows with Name column
#index =0
#for index,row in data.iterrows():
	#print(index,row['Name'])

print('\n')

#print all where Type 1 equals Poison
#print(data.loc[data['Type 1'] == "Poison"])
print('\n')

#get mean , min, std , max etc..
#data.describe()

#sort columns by attack ASCD
#print(data.sort_values('Attack'))
#DESC
#print(data.sort_values('Attack',ascending =False))
print('\n')


# Hockey data practice
hockey_data =pd.read_csv("skater_stats.csv",encoding = "ISO-8859-1",low_memory=False,
	dtype={'GP': int})
# sort by team asc and Goals Decs
print(hockey_data.sort_values(['Tm','G'],ascending=[1,0]))
print('\n')

# add columns G+A
hockey_data['G+ATotal']= hockey_data['G'] + hockey_data['A']
print(hockey_data[['Player','G+ATotal']])
print('\n')

#drop column G+ATotal
hockey_data = hockey_data.drop(columns=['G+ATotal'])

# add total #2
#" : " means all rows
hockey_data['G+ATotal'] =hockey_data.iloc[:,7:9].sum(axis=1)
print(hockey_data.head())

print('\n')

# if all values were numbers , this would work
#hockey_data['G']=hockey_data['G'].astype(int)

# some values in 'G' are problematic , convert those to NaN
hockey_data['G'] = pd.to_numeric(hockey_data['G'], errors='coerce')

# Get a Series object containing the data type objects of each column of Dataframe.
# Index of series is column name.
dataTypeHockey = hockey_data.dtypes
print('Data type of each column of Dataframe :')
print(dataTypeHockey)

print(hockey_data.head())
