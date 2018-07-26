# -*- coding: utf-8 -*-
#imported libraries 
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
#create empty list to store the info for each jobs
designation=[]  #for storing designation
org=[]          #for storing organization
exp=[]          #for expirience
loc=[]          #for loaction
skillset=[]     # to store skill set 

url="https://www.naukri.com/jobs-in-bangalore"
#looping 40 pages to gather around 2000 jobs 
for a in range(40):
    #making request to access resources using request module 
    req = Request(url+"-"+str(a), headers={'User-Agent': 'Mozilla/5.0'}) 
    #user-agent is set to mozillla /5.0 because we face authentication probkem when we use just urlopen module 
    html_doc = urlopen(req).read()
    #creating soup object to parser html script
    soup=BeautifulSoup(html_doc,'html.parser')
    #containers is list of all <div type="tuple">
    containers=soup.findAll("div",{"type":"tuple"})
    #loop through each containers in containers
    for container in containers:    
        designation.append(container.li['title'])
        org.append(container.find("span",{"class":"org"}).text)
        #check whelter None object or not to avoid attribute error 
        if container.find("span",{"class":"exp"}) is not None:
            exp.append(container.find("span",{"class":"exp"}).text)
        else:
            exp.append("None")
        
        loc.append(container.find("span",{"class":"loc"}).text)
        #check to avoid attribute error 
        if container.find('span',{'class':'skill'}) is not None:
            skillset.append(container.find('span',{'class':'skill'}).text)
        else:
            skillset.append("None")

#storing the dictionary of list to dataframe
table=pd.DataFrame({'Designation':designation,
                    'organijsation':org,
                    'location':loc,
                    'tenure':exp,
                    'skill':skillset})
    

print("\n")
#writing dataframe to excel file 
writer=pd.ExcelWriter('Banglore Job_Scrapper.xlsx')
table.to_excel(writer,"sheet1")
#saving excel file
writer.save()

