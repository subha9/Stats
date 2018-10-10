
# coding: utf-8

# In[ ]:


#Is gender independent of education level? A random sample of 395 people were
#surveyed and each person was asked to report the highest education level they
#obtained. The data that resulted from the survey is summarized in the following table:
#High School Bachelors Masters Ph.d. Total
#Female 60 54 46 41 201
#Male 40 44 53 57 194
#χ2=(60−50.886)2/50.886+⋯+(57−48.132)2/48.132Total 100 98 99 98 395
#Question: Are gender and education level dependent at 5% level of significance? In
#other words, given the data collected above, is there a relationship between the gender
#of an individual and the level of education that they have obtained?


# In[4]:


import numpy as np
import pandas as pd
import scipy.stats as stats


# In[5]:



Males = [40,44,53,57,194]
Females = [60,54,46,41,201]


# In[6]:


stats.chisquare(Males,Females)


# In[7]:



print("Since p-value is less than 0.05, we reject the NULL hypothesis that male and female are independent of each other")


# In[ ]:


Using the following data, perform a oneway analysis of variance using α=.05. Write up
the results in APA format.

[Group1: 51, 45, 33, 45, 67]
[Group2: 23, 43, 23, 43, 45]
[Group3: 56, 76, 74, 87, 56]


# In[13]:


Group1= [51, 45, 33, 45, 67]
Group2= [23, 43, 23, 43, 45]
Group3= [56, 76, 74, 87, 56]


# In[14]:


df = pd.DataFrame({"GroupA":Group1,"GroupB":Group2,"GroupC":Group3})


# In[15]:


df.head()


# In[ ]:


#ANOVA test has an important assumption that p-value to be valid must be satisfied in order for the associated 


# In[17]:


stats.f_oneway(Group1,Group2,Group3)


# In[ ]:



Since the p-value < 0.05 (alpha = 0.05),
the differences  between the means are statistically significant. 
Hence we reject the null hypothesis i.e. they may be equal


# In[ ]:


#Problem Statement 3:
#Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.
#For 10, 20, 30, 40, 50:

