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
    for a in a_tags:
        spans=a.find_all('span')
        div1=a.find('div')
        div2=div1.find('div')
        score_container=div2.find_all('div')[1]
        print((a))
        break
    #print(len(a_tags))
    away_team=(spans[0].text+" "+spans[1].text)
    home_team=(spans[2].text+" "+spans[3].text)
    date=(spans[7].text)
    #print(div2.text)

    #for div in score_container:#.find_all('div'):
    #    print(div.text)
    #print(len(score_container.find_all('div')))

    


getScoreStream('https://scorestream.com/team/pioneer-high-school-pioneers-8385/games')