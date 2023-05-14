#!/usr/bin/env python
# coding: utf-8

# # Cardio Good Fitness Case Study

# ## Introduction
# - The market research team at AdRight is assigned the task to identify the profile of the typical customer for each treadmill product offered by CardioGood Fitness.
# 
# - The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics.
# 
# - The team decides to collect data on individuals who purchased a treadmill at a CardioGoodFitness retail store during the prior three months.
# 
# - The data are stored in the CardioGoodFitness.csv file

# ## The team identifies the following customer variables to study:
# - product purchased, TM195, TM498, or TM798
# - gender;
# - age, in years;
# - education, in years;
# - relationship status, single or partnered;
# - annual household income ;
# - average number of times the customer plans to use the treadmill each week;
# - average number of miles the customer expects to walk/run each week;
# - self-rated fitness on an 1-to-5 scale, where 1 is poor shape and 5 is excellent shape.

# ## Descriptive Statistics
# ### Definition
# - Descriptive statistics are used to describe the basic features of the data in a study. They provide simple summaries about the sample and the measures. Together with simple graphics analysis, they form the basis of virtually every quantitative analysis of data.
# 
# - Descriptive statistics are typically distinguished from inferential statistics. With descriptive statistics we are simply describing what is or what the data shows. With inferential statistics, we are trying to reach conclusions that extend beyond the immediate data alone. 
#   - For instance, we use inferential statistics to try to infer from the sample data what the population might think. Or, we use inferential statistics to make judgments of the probability that an observed difference between groups is a dependable one or one that might have happened by chance in this study. Thus, we use inferential statistics to make inferences from our data to more general conditions; we use descriptive statistics simply to describe what’s going on in our data.
# 
# - Descriptive statistics provide a powerful summary that may enable comparisons across people or other units.
# 
# - Univariate Analysis :- It involves the examination of the single feature
# - The distribution is a summary of the frequency of individual values or ranges of values for a variable. The simplest distribution would list every value of a variable and the number of persons who had each value. 
#   - For instance, a typical way to describe the distribution of college students is by year in college, listing the number or percent of students at each of the four years. Or, we describe gender by listing the number or percent of males and females. In these cases, the variable has few enough values that we can list each one and summarize how many sample cases had the value. But what do we do for a variable like income or GPA? With these variables there can be a large number of possible values, with relatively few people having each one. In this case, we group the raw scores into categories according to ranges of values. For instance, we might look at GPA according to the letter grade ranges. Or, we might group income into four or five ranges of income values.
# 
# - The central tendency The central tendency of a distribution is an estimate of the “center” of a distribution of values. There are three major types of estimates of central tendency:
# 
#   - Mean 
#   - Median 
#   - Mode
# 
# - The dispersion, it refers to the spread of the values around the central tendency. There are two common measures of dispersion, the range and the standard deviation. 
#   - The range is simply the highest value minus the lowest value. In our example distribution, the high value is 36 and the low is 15, so the range is 36 - 15 = 21.
# 
#   - The Standard Deviation is a more accurate and detailed estimate of dispersion because an outlier can greatly exaggerate the range (as was true in this example where the single outlier value of 36 stands apart from the rest of the values. The Standard Deviation shows the relation that set of scores has to the mean of the sample. the formula for the standard deviation:
# 
#    - the square root of the sum of the squared deviations from the mean divided by the number of scores minus one.

# ## Importing libraries

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Loading the Dataset

# In[3]:


db = pd.read_csv('C:/Users/suman/Desktop/DS learn/Project/Study/CardioGoodFitness/CardioGoodFitness.csv')


# In[4]:


db.head()


# In[5]:


db.describe().T


# In[6]:


db.info()


# In[7]:


db.shape


# In[8]:


db.isna().any()


# ### No Missing values in the dataset.

# In[9]:


db.describe(include='all')


# In[10]:


db.hist(figsize=(20,20))


# ## Boxplots
# Which is the most popular model by gender?
# 
# 

# In[12]:


pd.crosstab(db['Product'],db['Gender'] )


# In[13]:


sns.boxenplot(x='Gender',y='Age',data=db)


# ### Seperated data by Gender.

# In[14]:


db.hist(by='Gender',column = 'Income')


# ### Gender v/s Miles

# In[22]:


db.hist(by='Gender',column = 'Miles')


# ### Product v/s miles

# In[23]:


db.hist(by='Product',column = 'Miles', figsize=(20,30))


# ### Average of age

# In[15]:


db['Age'].mean()


# In[16]:


sns.distplot(db['Age'])


# ## Count Plot
# - x= number of each product 
# - hue= seperated by Gender

# In[18]:


sns.countplot(x='Product',hue='Gender',data=db)


# ## Pairplot
# Quick overview of the data

# In[19]:


sns.pairplot(db)


# ## Corelation Heat Map

# In[20]:


corr=db.corr()
corr


# In[21]:


sns.heatmap(corr,annot=True)


# ## How do income and age affect the decision of which model is bought?
# We can infer that TM798 is the more expensive model

# In[24]:


sns.scatterplot(x='Age', y='Income',data=db, hue = 'Product')
plt.show()

