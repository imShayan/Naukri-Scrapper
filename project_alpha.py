# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:00:38 2018

@author: Kunal
"""

import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
url="https://www.naukri.com/python-jobs"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html_doc = urlopen(req).read()
soup=BeautifulSoup(html_doc,'html.parser')
containers=soup.findAll("div",{"type":"tuple"})

designation=[]
org=[]
time=[]
loc=[]
skillset=[]
stand=soup.find("div",attrs={'class':'desc'})
for container in containers:
    designation.append(container.li['title'])
    org.append(container.find("span",{"class":"org"}).text)
    time.append(container.find("span",{"class":"exp"}).text)
    loc.append(container.find("span",{"class":"loc"}).text)
    skillset.append(stand.select('span[skill]'))



table=pd.DataFrame({'post':designation,
                    'organijsation':org,
                    'location':loc,
                    'tenure':time,
                    'skill':skillset})
    

print("\n")
print(table.tail(2))
