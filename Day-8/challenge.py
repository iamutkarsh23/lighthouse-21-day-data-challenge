### Tutorial
**Pandas** is one of the most widely used Python plugins. Pandas can be used when working with large datasets, or when performing data cleaning, manipulation, and anlaysis. 

In this week of challenges we will be using some basic pandas functionalities to help us gain insights into the datasets we're working with.

But before we can use the pandas plugin, we have to import it.

Because pandas exists externally to basic Python, we need to import it. When importing, we give an alias to pandas so it shortens our code when calling on functions from pandas. Instead of writing ***pandas.name_of_function()*** we'll be able to write ***pd.name_of_function()***. The alias ***pd*** is standard within the Python community. 

The first pandas function we'll use is called with ***pd.read_csv()***. This function reads the path to a ***.csv*** file and stores in a pandas DataFrame. A pandas DataFrame is a representation of data in a table, similar to what we typically see when working within Excel. 

```
df = pd.read_csv('path/to/csv/sample.csv')
```

The second function we'll use is df.head(), which by default displays the top 5 rows of a dataframe. However, we can change that by inputting an integer value between the parentheses after .head with the number of rows we would like to observe.

```
df.head(21)
```

The third function we'll use is ***df.tail()***, which by default displays the bottom five rows of a dataframe. However, we can change that by inputting an integer value between the parentheses after *.tail* with the number of rows we would like to observe.

```
df.tail(4)
```
Try out the following functions on our pandas DataFrame *df*, and see what you can learn from the dataset. 

**DataFrame Functions**
- df.describe() *provides descriptive statistics of all numerical columns*
- df.unique() *Number of unique items in a column*
- df.shape() *gets the number of rows and columsn in the dataframe*

**DataFrame Column Functions**
- info() *provides an overview of all the columns, number of non-nulls, and data types in a DataFrame*
- max() *gets the max value from a column*
- min() *gets the min value from a column*
- mean() *get the mean value from a column*
- idxmax() *gets the integer index position of the max value from a column*
- idxmin() *gets the integer index position of the min value from a column*
- loc() *gets rows (or columns) with particular labels from the index*
- iloc() *gets rows (or columns) with particular positions in the index (only takes integers)*

```
#example using info()
df.info()

#example calling the max number from a column
df['column_name'].max()
```

To learn more about the various pandas functions, check out the user guide in the [pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide).


**Why should I use the documentation?**

On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. However, there are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work. 


### Challenge

After playing around with the functions above, you can start helping Dot figure out when the best time to rent a cow might be. With this dataset, you can take a look at how cows produce milk over time. 

Answer the following questions for Dot: 

1. At what year and month did company x produce the most milk?
2. At what year and month did company x produce the least milk? 

**Stretch**

*Stretch questions are not required to be completed for the challenge, but you can test your skills with more advanced challenges.*

1. Which year produced the most milk? 
