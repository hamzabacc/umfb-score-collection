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

    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    test_outer = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})


    '''
    CODE TO OBTAIN SCROLL CONTAINER + TAGS
    '''

    scroll_container=soup.find('div', attrs={'class':'ReactVirtualized__Grid__innerScrollContainer'})
    a_tags=scroll_container.find_all('a')
    football_game=False
    for a in a_tags:
        spans=a.find_all('span')
        for span in spans:
            if (span.text=='Boys Varsity Baseball'):
                football_game=True
        div1=a.find('div')
        div2=div1.find('div')
        score_container=div2.find_all('div')[1]
        if (football_game):
            break
    if (not football_game):
        return "No score available for the selected sport,"
    inners= div2.find_all('div',attrs={'style':"font-size: 48px; display: flex; position: relative; flex-direction: column;"})
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
    if(not final):
        return("score available is not a final score,")
    if(len(ints)>2):
        return("more than two score numbers pulled. check manually,")
    else:
        away_score=ints[0]
        home_score=ints[1]
    away_team=(spans[0].text+" "+spans[1].text)
    home_team=(spans[2].text+" "+spans[3].text)
    date=(spans[7].text)
    for span in spans: 
        print(span.text)
    return (home_team+','+str(home_score)+' to '+str(away_score)+','+away_team+','+date)

    


print(getScoreStream('https://scorestream.com/team/pioneer-high-school-pioneers-8385/games'))