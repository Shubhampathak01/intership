#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


# In[3]:


driver = webdriver.Chrome(r'C:\Users\bluechip\Downloads\chromedriver-py-120.0.6099.71\chromedriver_py\chromedriver_win64.exe')


# In[4]:


url= 'https://www.nike.com'


# In[5]:


driver.get(url)


# In[6]:


shoes= "https://www.nike.com/in/w/shoes-y7ok"


# In[7]:


driver.get(shoes)


# In[8]:


ShoeName=[]
Category=[]
Colors=[]
Price=[]


# In[9]:


try:
    shoe=driver.find_elements(By.XPATH,'//div[@class="product-card__title"]')
    for i in shoe:
        ShoeName.append(i.text)
except NoSuchElementException:
        ShoeName.append('_')
except StaleElementReferenceException:
        ShoeName.append('_')
        
try:
    category=driver.find_elements(By.XPATH,'//div[@class="product-card__subtitle"]')
    for i in category:
        Category.append(i.text)
except NoSuchElementException:
        Category.append('_')
except StaleElementReferenceException:
        Category.append('_')
        
try:
    color=driver.find_elements(By.XPATH,'//div[@class="product-card__product-count"]')
    for i in color:
        Colors.append(i.text)
except NoSuchElementException:
        Colors.append('_')
except StaleElementReferenceException:
        Colors.append('_')
        
try:
    price=driver.find_elements(By.XPATH,'//div[@class="product-card__animation_wrapper"]')
    for i in price:
        Price.append(i.text)
except NoSuchElementException:
        Price.append('_')
except StaleElementReferenceException:
        Price.append('_')
        


# In[10]:


a={'Shoes model name ': ShoeName,'Category in M/F ': Category, 'No. of colors': Colors,'Price in MRP':Price}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df

