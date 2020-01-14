import pandas as pd


data=pd.read_csv("pokemon_data.csv")
print(data.head(3))
print('\n')

data_xlsx=pd.read_excel("pokemon_data.xlsx")
print(data_xlsx.tail(3))
print('\n')

data_tabSep= pd.read_csv("pokemon_data.txt",delimiter='\t')
print(data_tabSep.head(4))
print('\n')

#print colums
#will print all
print(data[['Name','HP','Speed']])
print('\n')

#will print all details of index 0 only
print(data.iloc[0])
print('\n')

#or multiple rows ( will get rows 0 ,1 ,2)
print(data.iloc[0:3])
print('\n')

#get row 2 , column index 1
print(data.iloc[2,1])
print('\n')

#will print all rows with Name column
#index =0
for index,row in data.iterrows():
	print(index,row['Name'])

print('\n')

#print all where Type 1 equals Poison
print(data.loc[data['Type 1'] == "Poison"])
print('\n')

#get mean , min, std , max etc..
data.describe()

#sort columns by attack ASCD
print(data.sort_values('Attack'))
#DESC
print(data.sort_values('Attack',ascending =False))
print('\n')
