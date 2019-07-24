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

#path=r'C:\\Users\\Hamza\\Documents\\Football'
#driver = webdriver.Chrome(executable_path = path)
#path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
#driver = webdriver.Chrome(executable_path = path)
''' ^MAKE DRIVER AND PATH UNIVERSAL VARIABLES FOR USE ACROSS FXNS'''
#NO LONGER UNIVERSAL VARS FOR SAKE OF REUSING CHROME WEBDRIVER

EXECUTION_COUNT=0


def getScoreStream(url, sportKey):
    one_game=False
    #football_found = False
    path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)
    

    #NO LONGER IN USE
    '''CREATING CSV FILE DESTINATION'''
    global EXECUTION_COUNT
    FILE_TITLE="test_csv"+str(EXECUTION_COUNT)+'.csv'
    #f=open(FILE_TITLE,'w')
    '''^^if needed to make individual excel sheet for EACH GAME'''



    #url = input('Enter - ')
    #html = urlopen(url).read()
    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    test_outer = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})


    '''
    CODE TO OBTAIN SCROLL CONTAINER + TAGS
    '''

    #outer=soup.find('div', attrs={'class':'rmq-1c61845d'})
    #print(outer)  
    scroll_container=soup.find('div', attrs={'class':'ReactVirtualized__Grid__innerScrollContainer'})
    divs=scroll_container.find_all('div')

    a_tags=scroll_container.find_all('a')
    #print(len(a_tags))
    #sys.exit()  


    '''
    TESTNG DIV RETRIEVAL INSIDE OF DIVS
    '''


    print("\n\nAUTOMATED SCORE COLLECTION \n\n")

    i=0
    cs_scores=[]

    for a in a_tags:
        cs_score=""
        first_div=(a.find('div'))
        inner_div=first_div.find_all('div')
        raw_sport=(str(get_spans(a)))
        sport=('\n'+str(get_spans(a))+" Final Score:")
        if sportKey in sport:
            break