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
jobstr=""
#store list of all skills of all employ in a single string for regex parsing 
for skill in skillset:
    jobstr=jobstr + skill
print(jobstr)
#create an empty dictionary to store the frequency of occurence of each skills 
dk={}
#applying regex for fast and effiecient search  
sk1= re.compile(r'Management|management')
dk['s1']=len(sk1.findall(jobstr)

sk2=re.compile(r'Java|java')
dk['s2']=len(sk2.findall(jobstr))

sk3=re.compile(r'Python|python')
dk['s3']=len(sk3.findall(jobstr))

sk4=re.compile(r'PHP|php')
dk['s4']=len(sk4.findall(jobstr))
             
sk5=re.compile(r'marketing')
dk['s5']=len(sk5.findall(jobstr))
#make table to store the dictionary              
table2=pd.DataFrame(dk,index=[0])
print(table2)
#visualize the data using bar graph
ax=table2.plot(kind='bar' ,title='job analysis on skills',figsize=(15,10),legend=True,fontsize=10)
ax.set_xlabel('skills',fontsize=12)
ax.set_ylabel('jobs available',fontsize=12)
plt.show()

#writing dataframe to excel file 
writer=pd.ExcelWriter('Banglore Job_Scrapper.xlsx')
table.to_excel(writer,"sheet1")
#saving excel file
writer.save()

