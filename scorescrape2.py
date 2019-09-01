from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
import unittest
import requests
import sys as sys
import time
import os
import re


def getScoreStream(url, sportKey=""):
    path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)

    #time.sleep(2)


    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    #test_outer = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})


    '''
    CODE TO OBTAIN SCROLL CONTAINER + TAGS
    '''

    span_city_state=soup.find('span', attrs={'itemprop':'address'})
    city_state=span_city_state.text
    state=city_state[len(city_state)-2:]

    
    scroll_container=soup.find('div', attrs={'class':'ReactVirtualized__Grid__innerScrollContainer'})
    try:
        a_tags=scroll_container.find_all('a')
    except:
        time.sleep(5)
        html=driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        span_city_state=soup.find('span', attrs={'itemprop':'address'})
        city_state=span_city_state.text
        state=city_state[len(city_state)-2:]
        scroll_container=soup.find('div', attrs={'class':'ReactVirtualized__Grid__innerScrollContainer'})
        a_tags=scroll_container.find_all('a')
    TEAM_NAME=str(soup.find('h1').text)

    #return len(a_tags)
    football_game=False
    for a in a_tags:
        spans=a.find_all('span')
        for span in spans:
            if (sportKey in span.text):
                football_game=True
        div1=a.find('div')
        div2=div1.find('div')
        #score_container=div2.find_all('div')[1]
        if (football_game):
            break

    cancelled=False
    inners= div2.find_all('div',attrs={'style':"font-size: 48px; display: flex; position: relative; flex-direction: column;"})
    #return inners[0].find('div').text
    try: 
        if ("Cancelled" in inners[0].find('div').text):
            cancelled=True
    except: pass
    
    #return cancelled

    ints=[]
    final = False
    for tag in inners[0].find_all('div'):
        #print(tag.text)
        try:
            ints.append(int(tag.text))
        except:
            pass
        #try:
        if(tag.text==('Final')):
                final=True
        #except:pass
    
    away_team=(spans[0].text+" "+spans[1].text)
    home_team=(spans[2].text+" "+spans[3].text)

    two_scores=True
    date=(spans[7].text)
    if ("\'18" in date and "\'19" not in date):
        return TEAM_NAME+","+state+','+"N/A"+",no recent football scores available,"

    if cancelled:
        if(TEAM_NAME==(away_team)):
            return TEAM_NAME+','+state+','+'@'+home_team+","+'Cancelled,'+date+','
        else: return TEAM_NAME+','+state+','+'vs. '+away_team+','+'Cancelled,'+date+','

    if 'Last' not in date and 'Yesterday' not in date and 'Today' not in date:
        return TEAM_NAME+","+state+','+"N/A"+",most recent score isn't from this week"


    if(len(ints)>2):
        two_scores=False
    else:
        away_score=ints[0]
        home_score=ints[1]

    

    RESULT = ""
    outcome= ""
    opponent=""
    if TEAM_NAME==(away_team):
        opponent="@ " + home_team
        if(away_score>home_score):
            outcome='W '+str(away_score)+"-"+str(home_score)
        else: 
            if(home_score>away_score):
                outcome='L '+str(home_score)+"-"+str(away_score)
        RESULT=away_team+','+state+','+'@ '+str(home_team)+','+outcome+','+date
    else:
        if TEAM_NAME==(home_team):
            opponent="vs. " + away_team
            if(away_score>home_score):
                outcome='L '+str(away_score)+"-"+str(home_score)
            else: 
                if(home_score>away_score):
                    outcome='W '+str(home_score)+"-"+str(away_score)
        RESULT=home_team+','+state+','+'vs. '+str(away_team)+','+outcome+','+date
    driver.close()
    if not football_game:
        return TEAM_NAME+","+state+','+"N/A"+",no recent football scores available,"
    if not two_scores:
        return(TEAM_NAME+","+state+','+opponent+",more than two score numbers pulled. check manually,")
    if not final:
        return(TEAM_NAME+","+state+','+opponent+",score available is not a final score,"+date)
    
    
    
    return RESULT
    

#print(getScoreStream('https://scorestream.com/team/bergen-catholic-high-school-crusaders-243975/games','Boys Varsity Football'))  
#BE SURE TO ADD /games TO TESTING URLS!
#print(getScoreStream('https://scorestream.com/team/miami-central-senior-high-school-rockets-4021/games', 'Boys Varsity Football'))
#print(getScoreStream('https://scorestream.com/team/pinnacle-high-school-pioneers-1156/games','Boys Varsity Football'))
#print(getScoreStream('https://scorestream.com/team/st-louis-school-crusaders-242678/games', 'Boys Varsity Football'))