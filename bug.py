# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:21:40 2018

@author: Kunal
"""

#import librarys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
url='https://www.naukri.com/jobs-by-location'
#link created
req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
html_doc=urlopen(req).read()
#cfreating beautiful soup object
soup=BeautifulSoup(html_doc,'html.parser')
#testy is list  of all links in <a> tag
testy=soup.select('a[href*=".com/jobs-in-"]')
link_list=[]
for test in testy:
    link_list.append(test['href'])
    
#print(link_list[0])
#link_list has list of http:\\ of all cities
#loop through each link
designation=[]
org=[]
exp=[]
loc=[]
skillset=[]
append_groups=[]
for link in link_list:
    
    #loop through multiple pages in a link
    for a in range(2):
        
        reqq=Request(link +"-"+str(a),headers={'User-Agent':'Mozilla/5.0'}) 
        #open the url and read it
        html=urlopen(reqq).read()  
        nSoup=BeautifulSoup(html,'html.parser')  
        #container  contains all the div container or the jobs
        containers=nSoup.findAll("div",{"type":"tuple"})
        for container in containers:
            designation.append(container.li['title'])
            org.append(container.find("span",{"class":"org"}).text)
            exp.append(container.find("span",{"class":"exp"}))
            loc.append(container.find("span",{"class":"loc"}).text)
            skillset.append([container.div.find("span",{"class":"skill"})])
            
    table=pd.DataFrame({'post':designation,
                             'organijsation':org,
                             'location':loc,
                             'expirence':exp,
                             'skill':skillset})
    append_groups.append(table)

print(append_groups)