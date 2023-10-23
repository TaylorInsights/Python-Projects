#!/usr/bin/env python
# coding: utf-8

# ## Read in the file Popular_Baby_Names.csv

# In[57]:


import pandas as pd
popular_babynames = pd.read_csv("Popular_Baby_Names.csv")
popular_babynames.head()


# ## Print the shape and the first 10 rows to familiarize yourself with the data

# In[58]:


df = pd.DataFrame(popular_babynames)
print("Shape of the DataFrame:", df.shape)

rows = 10
print (f"First {rows} rows of the DataFrame:")
print (df.head(rows))


# ## Rename the "Year of Birth" & "Child's First Name" columns to remove the spaces and apostrophe. Explain why managing column names this way can be advantageous. The importance of renaming columns is to continue consistant patterns in code as well as naming conventions. I chose snake_case as it is my favorite way to reference code.

# In[59]:


df = df.rename(columns={'Year of Birth': 'Year_Of_Birth', "Child's First Name": 'Childs_First_Name'})
df.head() 


# ## Print the data types and describe if they are appropriate for analysis or need to be converted to other types. If they need to be converted, perform the conversions. The data types listed as integers "Count" and "Rank" are appropriate data types as they represent numeric/integer values. Also "Gender", "Ethnicity" and "Childs_First_Name" are also appropriate as objects as they are represented as strings. I changed Year_Of_Birth from an Int to an Obj as we do not add years together.

# In[60]:


print("Data Types of the file Popular Baby Names are:")
print(df.dtypes)
print()
print("The Updated Data Types of the file Popular Baby Names are:")
df['Year_Of_Birth'] = df['Year_Of_Birth'].astype('object')
print(df.dtypes)


# ## After reviewing the data, clean the data as you see appropriate. For this cleaning step, you do not need to show all your work or interim results as you examine the data, but you do need to show any commands you used to alter any of the data in the order you use them.

# In[61]:


#this definition combines duplications of ethnicity names that appear
def group_ethnicities(df):
    for index, row in df.iterrows():
        if 'ASIAN AND PACI' in row['Ethnicity']:
            df.loc[index, 'Ethnicity'] = 'ASIAN AND PACIFIC ISLANDER'
        elif 'BLACK NON HISP' in row['Ethnicity']:
            df.loc[index, 'Ethnicity'] = 'BLACK NON HISPANIC'
        elif 'WHITE NON HISP' in row['Ethnicity']:
            df.loc[index, 'Ethnicity'] = 'WHITE NON HISPANIC'
    return df

df = group_ethnicities(df)

#this makes sure the objects in Childs_First_Name are uniform
df['Childs_First_Name'] = df['Childs_First_Name'].str.lower()

#this drops any duplicate rows that appear
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)


# ## Print and explain basic descriptive statistics. Both grid/numeric styles and graphic/chart styles can be helpful.

# In[62]:


import matplotlib.pyplot as mat

#Using the describe feature generates stats that calculates the count, mean, standard deviation, min,
#25th percentile, 50th percentile, 75th percentile and max. This is for Integer Data Types.

print(df_no_duplicates.describe())


#Using the BarChart feature generates stats for Object Data Types.

mat.figure(figsize=(10, 6))
df_no_duplicates['Year_Of_Birth'].value_counts().sort_index().plot(kind='bar')
mat.title('Bar Chart for Year_Of_Birth')
mat.xlabel('Year_Of_Birth')
mat.ylabel('Count')
mat.show()

mat.figure(figsize=(10, 6))
df_no_duplicates['Gender'].value_counts().sort_index().plot(kind='bar')
mat.title('Bar Chart for Gender')
mat.xlabel('Gender')
mat.ylabel('Count')
mat.show()

mat.figure(figsize=(10, 6))
df_no_duplicates['Ethnicity'].value_counts().sort_index().plot(kind='bar')
mat.title('Bar Chart for Ethnicity')
mat.xlabel('Ethnicity')
mat.ylabel('Count')
mat.show()

top = 10  # Change the number to control the number of names displayed
top_names = df_no_duplicates['Childs_First_Name'].value_counts().head(top)

mat.figure(figsize=(10, 6))
top_names.plot(kind='bar')
mat.title(f'Top {top} Childs_First_Name')
mat.xlabel('Childs_First_Name')
mat.ylabel('Count')
mat.show()


# ## Determine how many unique names are in the data. This should be the number of unique names within the entire dataset – i.e. not specific to year, gender, or ethnicity.

# In[63]:


unique_name_count = df_no_duplicates['Childs_First_Name'].nunique()
print("Number of unique names:", unique_name_count)


# ## Do a multicolumn sort of Rank + Year + Gender + Ethnicity. Print the first 60 rows.

# In[64]:


multi_sort = df_no_duplicates.sort_values(by=['Rank', 'Year_Of_Birth', 'Gender', 'Ethnicity'])
print(multi_sort.head(60))


# ## Print the ten most popular (greatest count) names in descending order by total count. This should be the most popular names within the entire dataset – i.e. not specific to year, gender, or ethnicity.

# In[65]:


grouped_df = df_no_duplicates.groupby('Childs_First_Name')['Count'].sum().reset_index()
grouped_df.rename(columns={'Count': 'Total_Count'}, inplace=True)
grouped_df = grouped_df.sort_values(by='Total_Count', ascending=False)
top_10_grouped_df = grouped_df.head(10)
print(top_10_grouped_df)


# ## Print the ten most popular (greatest count) names for each gender, not specific to year or ethnicity in descending order by total count

# In[66]:


grouped_df = df_no_duplicates.groupby(['Childs_First_Name', 'Gender'])['Count'].sum().reset_index()
grouped_df.rename(columns={'Count': 'Total_Count'}, inplace=True)
grouped_df['Rank'] = grouped_df.groupby('Gender')['Total_Count'].rank(ascending=False, method='first')
grouped_df = grouped_df.sort_values(by=['Gender', 'Total_Count'], ascending=[True, False])
top_10_by_gender = grouped_df[grouped_df['Rank'] <= 10]
for gender, group in top_10_by_gender.groupby('Gender'):
    print(f"Top 10 names for {gender} in descending order:")
    print(group)
    print("\n")


# ## Determine how many names were recorded 10 or fewer times. This should be the least popular names within the dataset – i.e. not specific to year, gender or ethnicity.
# 

# In[67]:


name_counts = df_no_duplicates.groupby('Childs_First_Name')['Count'].sum()
least_popular_names = name_counts[name_counts <= 10]
count_of_least_popular_names = len(least_popular_names)
print("Names recorded 10 or fewer times:", count_of_least_popular_names)


# In[ ]:




