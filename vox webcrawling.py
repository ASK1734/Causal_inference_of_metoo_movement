import requests
import datetime as dt
import pandas as pd
import numpy as np
import time
from datetime import datetime
from bs4 import BeautifulSoup

resp = requests.get('https://www.vox.com/a/sexual-harassment-assault-allegations-list')
soup = BeautifulSoup(resp.text, 'html.parser')

predator_name_list = []
divs = soup.find_all('div','col')

for div in divs:
    names = div.find_all('a')
    for name in names:
        name = name.text.strip() #print(name)
        predator_name_list.append(name) #print(result1) 


public_date_list = []
divs1 = soup.find_all('div','info-body')

for div in divs1:
    date_with_space = div.p.text.strip()
    date_lists = date_with_space.split()
    date = ""
    for date_list in date_lists:
        date = date + date_list + " "
        date = date.replace('Publicly reported ',"")
    public_date_list.append(date)


#犯了什麼錯

crime_content_list = []
divs1 = soup.find_all('div','info-body')

for div in divs1:
    crimes = div.find_all('p')[1].text.strip()
    crime_content_list.append(crimes)
    #print(crimes)
#print(result3)


victim_name_list = []
victims = soup.find_all('footer')

for victim in victims:
    
    try:
        name = victim.strong.text.strip().replace(',','')
        #print(victim.a)
        #print(victim.a.text.strip())
        victim_name_list.append(name)
    
    except:
        if victim.a.text.strip() == "":
            continue
        else:
            name = victim.a.text.strip().replace(',','')
            victim_name_list.append(name)


victim_career_list = []
victims = soup.find_all('footer')

for victim in victims:
    
        careers = victim.a.text.strip().split(", ")

        try:
            victim_career_list.append(careers[1])
            #print(careers[1])
        except:
            
            if careers[0] == "":
                continue
            else:
                victim_career_list.append('Unknown')
                #print('unknown')


sources = soup.find_all('p','small')

person_all_links = ""
n = 0
more_info = []

for source in sources:
        source = source.find_all('a','ref')
        link_of_s = []
        for s in source:
                
                alllink = s['href']
                strlink = str(alllink)
                link_of_s.append(strlink)
        
        for link in link_of_s:
                
                n=n+1
                if len(link_of_s) == 1:
                        person_all_links = link+'\n'
                        
                elif len(link_of_s)>1:
                        if n>1:
                                person_all_links = person_all_links+link+'\n'
                                
                        elif n == 1:
                                person_all_links = link+'\n'
                                
        n=0                
        
        more_info.append(person_all_links)
        
data = {'predator':predator_name_list,
        'predator career':predator_career_list,
        'victim':victim_name_list,
        'victum career':victim_career_list, 
        'Public date':public_date_list,
        'crime content':crime_content_list,
        'source/more info':more_info}

df = pd.DataFrame(data) 

import sqlite3
  
conn = sqlite3.connect('MeToo.db')  #建立資料庫
cursor = conn.cursor()
cursor.execute('DROP TABLE rawdata') #直接砍掉舊Table，因為有時候會有新增column什麼的
cursor.execute('CREATE TABLE rawdata(predator, "predator career", victim, "victum career", "Public date", "crime content", "source/more info")')  #建立資料表
conn.commit()

#如果資料表存在，就寫入資料，否則建立資料表
df.to_sql('rawdata', conn, if_exists='append', index=False) 
 
#透過SQL語法讀取資料庫中的資料
us_df = pd.read_sql("SELECT * FROM rawdata WHERE victim='anonymous'", conn)
print(us_df)