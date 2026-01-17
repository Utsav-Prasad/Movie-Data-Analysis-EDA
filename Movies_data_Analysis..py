#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing important libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[3]:


df=pd.read_csv("mymoviedb.csv",lineterminator='\n')


# In[4]:


df.head()


# In[5]:


df.info()


# # release date is string type , but it should be datetime format.

# Our data donot contains null value , some columns such as poster_url , overview, and original_language may need to drop,

# In[6]:


#  exploring genre columns.
df['Genre'].head()


# In[7]:


df['Genre'].unique()


# Genre are separated by commas and separated by whitespaces

# In[8]:


df['Genre'].duplicated().sum()


# In[9]:


df['Genre'].nunique()


# In[10]:


df['Genre'].value_counts()


# In[11]:


#check for duplicates row
df.duplicated().sum()


# In[12]:


df.describe()


# • Exploration Summary
# • we have a dataframe consisting of 9827 rows and 9 columns.
# • our dataset looks a bit tidy with no NaNs nor duplicated values.
# • Release_Date column needs to be casted into date time and to extract only the
# • Overview, Original_Languege and Poster-Url wouldn't be so useful during analys
# • there is noticable outliers in Popularity column
# • Vote_Average bettter be categorised for proper analysis.
# • Genre column has comma saperated values and white spaces that needs to be hand

# In[13]:


#casting re.lease date value into year
df.head()


# In[14]:


df['Release_Date']=pd.to_datetime(df['Release_Date'],format='%Y-%m-%d',errors='coerce')
print(df['Release_Date'].dtypes)


# In[15]:


# df['Release_Date'] = pd.to_datetime(
#     df['Release_Date'],
#     errors='coerce'
# )


# In[16]:


df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtypes)


# In[17]:


df.info()


# In[18]:


df.head(1
       )


# Droping Overview, Original_Language and Poster_Url

# In[19]:


#create a list of columns that needs to be droped.
cols_drop=['Overview','Original_Language','Poster_Url']


# In[20]:


df.drop(cols_drop,axis=1,inplace=True)


# In[21]:


df.info()


# In[22]:


df.sample(5)


# In[23]:


df['Vote_Average'].describe()


# categorizing Vote_Average column
# We would cut the Vote_Average values and make 4 categories: popular average
# below_avg not_popular to describe it more using catigorize_col() function
# provided above.

# In[24]:


# def categorize_col(df,col,labels):
#     edges=[df[col].describe()['min'],df[col].describe()['25%'],
#           df[col].describe()['50%'],df[col].describe()['75%'],
#           df[col].describe()['max']]
#     df[col] = pd.cut(df[col], edges, labels,duplicates='drop')
#     return df
# labels=['not_popular', 'below_avg', 'average', 'popular']
# categorize_col(df,'Vote_Average',labels)


# In[25]:


def categorize_col(df, col, labels):
    # 1. Get the edges (Calculating once is faster)
    stats = df[col].describe()
    edges = [stats['min'], stats['25%'], stats['50%'], stats['75%'], stats['max']]
    
    # 2. Use include_lowest=True 
    # Without this, any row equal to the 'min' value becomes NaN
    df[col] = pd.cut(df[col], bins=edges, labels=labels, include_lowest=True)
    
    return df

labels = ['not_popular', 'below_avg', 'average', 'popular']
df = categorize_col(df, 'Vote_Average', labels)

# Verify the result
print(df['Vote_Average'].value_counts())


# In[26]:


# labels = ['not_popular', 'below_avg', 'average', 'popular']

# df['Vote_Category'] = pd.qcut(
#     df['Vote_Average'],
#     q=4,
#     labels=labels,duplicates='drop'
# )


# In[27]:


df['Vote_Average'].unique()


# In[28]:


df.head()


# In[29]:


df.isna().sum()
df.dropna()


# In[30]:


df.isna().sum()


# We want each column contains only one genre its totally fine , if we have same movie at multiple column

# In[31]:


#split the string into lists
df['Genre']=df['Genre'].str.split(", ")
#explode the list
df=df.explode('Genre').reset_index(drop=True)
df.head()


# In[32]:


df.info()


# In[33]:


df.nunique()


# Now that our dataset is clean and tidy, we are left with a total of 6 columns and 25551
# rows to dig into during our analysis

# # Data Visualization

# we'd use Matplotlib and seaborn for making some informative visuals to gain
# insights abut our data.

# In[34]:


# setting up seaborn configurations
sns.set_style('whitegrid')


# # Q1: What is the most frequent genre in
# the dataset?

# In[35]:


df['Genre'].describe()


# In[36]:


# visualizing genre column
sns.catplot(y = 'Genre', data = df, kind = 'count',
 order = df['Genre'].value_counts().index,
 color = '#4287f5')
plt.title('genre column distribution')
plt.show()


# # Q2.Which Genre has the highest vote?

# In[45]:


# visualizing vote_average column
sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
 order = df['Vote_Average'].value_counts().index,
 color = '#4287f5')
plt.title('votes destribution')
plt.show()


# # Q3: What movie got the highest popularity ? what's its
# genre ?

# In[53]:


df[df['Popularity']==df['Popularity'].max()].iloc[0]


# Q4: What movie got the lowest popularity? what's
# its genre?

# In[56]:


df[df['Popularity'] == df['Popularity'].min()]


# In[57]:


df.sort_values('Popularity', ascending=True).head(5)'''Since there is error in dataset that all popularity value is same that why this question 
can't be solved'''


# # Q5: Which year has the most filmmed movies?

# In[58]:


df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()


# Q1: What is the most frequent genre in the dataset?
# Drama genre is the most frequent genre in our dataset and has appeared more than
# 14% of the times among 19 other genres.
# Q2: What genres has highest votes ?
# we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the
# highest popularity among fans by being having more than 18.5% of movies popularities.
# Q3: What movie got the highest popularity ? what's its genre ?
# Spider-Man: No Way Home has the highest popularity rate in our dataset and it has
# genres of Action , Adventure and Sience Fiction .
# Q4: Which year has the most filmmed movies?
# year 2020 has the highest filmming rate in our dataset.
# 

# In[ ]:




