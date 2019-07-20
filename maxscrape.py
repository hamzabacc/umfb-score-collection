

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import ssl
import unittest
import requests
import sys as sys
import time
import os
import re

def getMaxPreps(url):
    path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)
    
    '''CREATING CSV FILE DESTINATION
    global EXECUTION_COUNT
    FILE_TITLE="test_csv"+str(EXECUTION_COUNT)+'.csv'
    #f=open(FILE_TITLE,'w')
    ^^if needed to make individual excel sheet for EACH GAME'''



    #url = input('Enter - ')
    #html = urlopen(url).read()
    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    schedule = soup.find('table', attrs={'id':"schedule"})
    gameContents = (schedule.find('tbody'))
    games = gameContents.findAll('tr')
    print(len(games))

    for game in games: 
        #print(game)
        #break
        try:
            data = game.findAll('td')
            for point in data:
                print(point.text)
                print('\n\n--------------\n')
            break
        except: pass


(getMaxPreps('https://www.maxpreps.com/high-schools/pioneer-pioneers-(ann-arbor,mi)/football-fall-18/schedule.htm'))
