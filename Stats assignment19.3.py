
# coding: utf-8

# In[3]:


#Problem Statement 1: Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25. For 10, 20, 30, 40, 50:

import numpy as np
import pandas as pd
import scipy.stats as stats


# In[4]:



group1 = [10,20,30,40,50]
group2 = [5,10,15,20,25]


# In[5]:


series1 = pd.Series(group1)
series2 = pd.Series(group2)# F-Teset
f = series1.var() / series2.var()
print(f)

