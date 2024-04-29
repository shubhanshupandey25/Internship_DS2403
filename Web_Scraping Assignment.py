#!/usr/bin/env python
# coding: utf-8

# # 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.

# In[494]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[419]:


page=requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[420]:


soup=BeautifulSoup(page.content)
soup


# In[421]:


movies= soup.find_all('div',class_="lister-item-content")
Name=[]
for i in movies:
    name=i.find('h3',class_="lister-item-header").a.text
    Name.append(name)
Name


# In[422]:


movies= soup.find_all('div',class_="lister-item-content")
Rank=[]
for i in movies:
        rank=i.find('h3',class_="lister-item-header").get_text(strip=True).split('.')[0]
        Rank.append(rank)
Rank


# In[423]:


movies= soup.find_all('div',class_="lister-item-content")
Year=[]
for i in movies:
        year=i.find('h3',class_="lister-item-header").find('span',class_="lister-item-year text-muted unbold").text.strip('()')
        Year.append(year)
Year


# In[424]:


movies= soup.find_all('div',class_="lister-item-content")
Rating=[]
for i in movies:
        rating=i.find('div',class_="ipl-rating-widget").find('span',class_="ipl-rating-star__rating").text
        Rating.append(rating)
Rating


# In[425]:


print(len(Name),len(Rank),len(Year),len(Rating))


# In[526]:


import pandas as pd
df=pd.DataFrame({'rank':Rank,'name':Name,'year':Year,'rating':Rating})
df


# # 4) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[506]:


page=requests.get('https://www.patreon.com/coreyms')
page


# In[507]:


soup=BeautifulSoup(page.content)
soup


# In[508]:


heading=[]
for i in soup.find_all('div',class_="sc-bUbRBg DYKxE"):
    heading.append(i.text)
heading    


# In[516]:


#DATA NOT FETCHING FROM THE CONTENT FROM THE ABOVE PATREON WEBSITE


# # 5) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji Nagar.

# In[442]:


page=requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar')
page


# In[443]:


soup=BeautifulSoup(page.content)
soup


# In[445]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Price=[]
for i in house:
    price=i.find_all('div',class_="font-semi-bold heading-6")[0].text
    Price.append(price)
Price


# In[415]:


Title=[]
for i in soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0"):
    Title.append(i.text)
Title    


# In[416]:


Location=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    Location.append(i.text)
Location


# In[446]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Emi=[]

for i in house:
    emi=i.find_all('div',class_="font-semi-bold heading-6")[1].text
    Emi.append(emi)
Emi


# In[447]:


house=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
Area=[]

for i in house:
    area=i.find_all('div',class_="font-semi-bold heading-6")[2].text
    Area.append(area)
Area


# In[448]:


(len(Area),len(Price),len(Emi),len(Title),len(Location))


# In[449]:


df=pd.DataFrame({'Title':Title,'Location':Location,'Price':Price,'Emi':Emi,'Area':Area})
df


# In[ ]:





# # 6) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .

# In[521]:


page=requests.get('https://www.bewakoof.com/bestseller?sort=popular%20.')
page


# In[522]:


soup=BeautifulSoup(page.content)
soup


# In[523]:


name=[]
for i in soup.find_all('h2',class_="clr-shade4 h3-p-name undefined false"):
    name.append(i.text)
name


# In[524]:


price=[]
for i in soup.find_all('div',class_="discountedPriceText clr-p-black false"):
    price.append(i.text)
price


# In[525]:


image=[]
for i in soup.find_all('div',class_="productCardImg false"):
    image.append(i.img['src'])
image


# In[527]:


df=pd.DataFrame({'Name':name,"Price":price,'Image':image})
df


# # 7) Please visit https://www.cnbc.com/world/?region=world and scrap

# In[450]:


page=requests.get('https://www.cnbc.com/economy/')
page


# In[451]:


soup=BeautifulSoup(page.content)
soup


# In[452]:


Heading=[]
for i in soup.find_all('div',class_="Card-titleContainer"):
    Heading.append(i.text)
Heading    


# In[454]:


Date=[]
for i in soup.find_all('span',class_="Card-time"):
    Date.append(i.text)
Date    


# In[472]:


import numpy as np


# In[474]:


link=[]
for i in soup.find_all('div',class_="Card-mediaContainer"):
    link.append(i.img['src'])
link


# In[486]:


df=pd.DataFrame({'Heading':Heading,'Date':Date})
df


# # Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/ and scrap-
#  a) Paper title
#  b) date
#  c) Author

# In[510]:


page=requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-%20%20%20%20%20articles/')
page


# In[511]:


# ABOVE ERROR


# # 2) Write a python program to scrape product name, price and discounts from
# https://peachmode.com/search?q=bags

# In[517]:


page=requests.get('https://peachmode.com/collections/new-arrival')
page


# In[518]:


soup=BeautifulSoup(page.content)
soup


# In[519]:


product=[]
for i in soup.find_all('div',class_="product-title"):
    product.append(i.text)
product    


# In[520]:


#DATA NOT FETCHING FROM THE CONTENT FROM THE ABOVE PEACHMODE WEBSITE


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




