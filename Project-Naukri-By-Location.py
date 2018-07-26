# -*- coding: utf-8 -*-

#import librarys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
#from urllib.error import HTTPError

url='https://www.naukri.com/jobs-by-location'
#link created
req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
html_doc=urlopen(req).read()
#creating beautiful soup object
soup=BeautifulSoup(html_doc,'html.parser')
#testy is list  of all links in <a> tag
testy=soup.select('a[href*=".com/jobs-in-"]')
link_list=[]
for test in testy:
    link_list.append(test['href'])
    
print(len(link_list))
#link_list has list of http:\\ of all cities
#loop through each link
append_groups=[]
for link in link_list:
    #create empty list to store info of each jobs
    designation=[]
    org=[]
    exp=[]
    loc=[]
    skillset=[]
    
    #loop through multiple pages in a link
    for a in range(10):
        req=Request(link +"-"+str(a),headers={'User-Agent':'Mozilla/5.0'}) 
        #open the url and read it
        html=urlopen(req).read() 
        Soup=BeautifulSoup(html,'html.parser')  
        #container  contains all the div container or the jobs
        containers=Soup.findAll("div",{"type":"tuple"})
        #loop through each containers
        for container in containers:
            #appending list 
            designation.append(container.li['title'])
            #appending the text of span class which has class attribute org
            org.append(container.find("span",{"class":"org"}).text)
            #conditional statement to check whelter object is None type or not in order to remove attribute error
            if container.find("span",{"class":"exp"}) is not None:
                exp.append(container.find("span",{"class":"exp"}).text)
            else:
                exp.append("None")
            
            loc.append(container.find("span",{"class":"loc"}).text)
            #conditional statement to avoid attribute error
            if container.find('span',{'class':'skill'}) is not None:
                skillset.append(container.find('span',{'class':'skill'}).text)
            else:
                skillset.append("None")
    #storing the dictionary of list in a data frame name table             
    table=pd.DataFrame.from_dict({'post':designation,
                                      'organijsation':org,
                                      'location':loc,
                                      'expirence':exp,
                                      'skill':skillset})
    
    #appending the multiple dataframe of each link into a list 
    append_groups.append(table)
#concatinating multiple dataframe into a single data frame     
results=pd.concat(append_groups)
#writing the dataframe into an excel sheet 
writer=pd.ExcelWriter("JOBS BY lOCATION.xlsx")
results.to_excel(writer,'sheet1')
#saving the excel sheet 
writer.save()