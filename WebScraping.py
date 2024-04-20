#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# 1) Write a python program to display all the header tags from wikipedia.org

# In[3]:


page=requests.get('https://www.wikipedia.org/')
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


#scraping header tags from wikipedia
header=[]
for i in soup.find_all('span',class_="other-project-title jsl10n"):
     header.append(i.text)
header    


# In[7]:


print(len(header))


# In[8]:


import pandas as pd
df=pd.DataFrame({'Headers':header})
df


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year
# of release) and make data frame

# In[28]:


Page=requests.get('https://www.imdb.com/list/ls091520106/')
Page


# In[31]:


Soup=BeautifulSoup(Page.content)
Soup


# In[37]:


#scaping movie names
name=[]
for i in soup.find_all('div',class_="lister-item-content"):
    name.append(i.text)
name


# In[41]:


rating=[]
for i in soup.find_all('div',class_="ipl-rating-star small"):
     rating.append(i.item)
rating


# In[39]:


year=[]
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
     year.append(i.text)
year


# In[40]:


print(len(name),len(rating),len(year))


# In[42]:


import pandas as pd
df=pd.DataFrame({'Name':name,'Rating':rating,'Year':year})
df


# 3) Write a python program to scrape mentioned details from dineout.co.in : i) Restaurant name
# ii) Cuisine iii) Location iv) Ratings v) Image URL.

# In[43]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page


# In[44]:


soup=BeautifulSoup(page.content)
soup


# In[45]:


name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    name.append(i.text)
name    


# In[46]:


cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
cuisine


# In[47]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[50]:


rating=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[52]:


image=[]
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
image


# In[53]:


print(len(name),len(cuisine),len(location),len(rating),len(image))


# 4) Write s python program to display list of respected former finance minister of India(i.e.
# Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make
# data frame.

# In[2]:


page=requests.get('https://presidentofindia.nic.in/former-presidents')
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[14]:


name=[]
for i in soup.find_all('div',class_="desc-sec"):
    name.append(i.text.replace('\n',' : '))
name


# In[15]:


import pandas as pd
df=pd.DataFrame({'Name':name})
df


# In[ ]:




