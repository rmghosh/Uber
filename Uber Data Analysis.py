#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Loading data file
# 

# In[11]:


Uberdata = pandas.read_csv('Desktop/Uber.csv')


# In[13]:


Uberdata.head()


# In[14]:


Uberdata


# In[15]:


Uberdata ['Date/Time']


# In[20]:


Uberdata['Date/Time'] = Uberdata['Date/Time'].map(pandas.to_datetime)


# In[22]:


Uberdata.tail()


# In[31]:


def get_dom(dt):
    return dt.day

Uberdata['dom'] = Uberdata['Date/Time'].map(get_dom)


# In[32]:


Uberdata


# In[25]:


dt = Uberdata['Date/Time'][50000]


# In[26]:


dt.day


# In[35]:


def get_weekday(dt):
    return dt.weekday()

Uberdata['weekday'] = Uberdata['Date/Time'].map(get_weekday)

Uberdata


# In[36]:


def get_hour(dt):
    return dt.hour

Uberdata['hour'] = Uberdata['Date/Time'].map(get_hour)

Uberdata


# # ANALYSIS

# # Analyze DOM

# In[42]:


hist(Uberdata.dom, bins = 30, rwidth = 0.8, range = (0.5, 30.5))
xlabel('Date of the month')
ylabel('Frequency')
title('Frequency by Dom - April 2014')


# In[45]:


for k, rows in Uberdata.groupby('dom'):
    print((k, len(rows)))


# In[46]:


def count_rows(rows):
    return len(rows)

by_date = Uberdata.groupby('dom').apply(count_rows)
by_date


# In[47]:


bar(range(1,31), by_date)


# In[49]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[52]:


bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('Date of the month')
ylabel('Frequency')
title('Frequency by Dom - April 2014')
("")


# # Analysis hour

# In[53]:


hist(Uberdata.hour, bins = 24, range= (.5,24))


# In[ ]:





# # Analyze weekday

# In[58]:


hist(Uberdata.weekday, bins =7, range= (-.5,6.5), rwidth =.8, color = 'green')


# In[ ]:





# # Cross Analysis (hour, dow)

# In[65]:


by_cross = Uberdata.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[66]:


seaborn.heatmap(by_cross)


# # by lat and lon

# In[69]:


hist(Uberdata['Lat'], bins = 100, range = (40.5, 41))
("")


# In[76]:


hist(Uberdata['Lon'], bins = 100, range = (-74.1, -73.9), color ='g', alpha =.5, label = 'Longitude')
legend(loc = 'upper left')
twiny()
hist(Uberdata['Lat'], bins = 100, range = (40.5, 41), color ='r', alpha =.5, label = "Latitude")
legend(loc='best')
("")


# In[78]:


plot(Uberdata['Lat'],'.', ms=10, color = 'green')
plot(Uberdata['Lon'],'.', ms=10, color = 'blue')
xlim(0,100)


# In[81]:


plot(Uberdata['Lon'], Uberdata['Lat'], '.', ms = 1, alpha =.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[83]:


figure(figsize =(20, 20))
plot(Uberdata['Lon'], Uberdata['Lat'], '.', ms = 1, alpha =.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




