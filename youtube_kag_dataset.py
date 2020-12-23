import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sas


def impute_med(series):
	return series.fillna(series.median())


df = pd.read_csv("https://raw.githubusercontent.com/DivyaThakur24/GoogleAppRating-DataAnalysis/master/googleplaystore.csv")

print(df.head())

print(df.shape)
print(df.describe())

"""print(df.info()) # to check number of non-null values

print(df.isnull()) #to check if a value is null or not"""

print(df.isnull().sum()) #sum of null values

print(df[df.Rating>5]) #to check rating greater than 5 

df.drop([10472], inplace=True) #to delete the row

print(df[10470:10475])# to check if row is deleted 

df.hist()



#plt.savefig("Matfig.png")

#threshold = len(df)*0.1

#df = df.dropna(thresh = threshold , axis = 1, inplace= True)


#data manipulation 

df.Rating = df['Rating'].transform(impute_med)

print(df.isnull().sum())

df["Type"].fillna(str(df["Type"].mode()), inplace=True)

df['Current Ver'].fillna(str(df['Current Ver'].mode()), inplace = True)

df['Android Ver'].fillna(str(df['Android Ver'].mode()), inplace = True)

print(df.isnull().sum())

df['Price'] = df['Price'].apply(lambda x : str(x).replace('$', '') if '$' in str(x) else str(x))

df['Price'] = df['Price'].apply(lambda x : float(x))

#print(df['Price'])

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

df['Installs'] = df['Installs'].apply(lambda x : str(x).replace('+', '') if '+' in str(x) else str(x))

df['Installs'] = df['Installs'].apply(lambda x : str(x).replace(',', '') if ',' in str(x) else str(x))


df['Installs'] = df['Installs'].apply(lambda x : float(x))

grp = df.groupby("Category")

x = grp['Rating'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Installs'].agg(np.sum)


plt.plot(x)
plt.xticks(rotation=90)
plt.savefig('Rat_plot.png')

plt.plot(y)
plt.xticks(rotation=90)
plt.savefig('Pric_plot.png')


plt.plot(z)
plt.xticks(rotation=90)
plt.savefig('Ins_plot.png')


#print(x)