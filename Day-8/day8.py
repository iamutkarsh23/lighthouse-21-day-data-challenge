import pandas as pd # pd is the alias we have given to pandas.
#To Read a Dataset
#Milk.csv is stored into a Pandas DataFrame variable called df.
df = pd.read_csv('milk.csv')

#df.head() function displays the first 5 rows of the dataset
df.head()
print(df['Month'].iloc[df['Monthly milk production: pounds per cow'].idxmax()]) # Ques1
print(df['Month'].iloc[df['Monthly milk production: pounds per cow'].idxmin()]) # Ques2

# Answers
# 19-Jun
# 07-Dec