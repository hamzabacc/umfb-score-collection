# To run this, you need to install BeautifulSoup if you aren't using anaconda
# https://pypi.python.org/pypi/beautifulsoup4
#import urllib

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

#path=r'C:\\Users\\Hamza\\Documents\\Football'
#driver = webdriver.Chrome(executable_path = path)
path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
''' ^MAKE DRIVER AND PATH UNIVERSAL VARIABLES FOR USE ACROSS FXNS'''


def getFootballGames(url):
    #path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    #driver = webdriver.Chrome(executable_path = path)
    driver.get(url)
    
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
    tag_dict={}
    for a in a_tags:
        tag_dict[a]=[]
        first_div=(a.find('div'))
        inner_div=first_div.find_all('div')
        sport=(str(get_spans(a))+" Final Score:")
        if "Boys" in sport:
            print(sport)
            for item in inner_div:
                try:
                    #print(item.text)
                    num=int(item.text)
                    print(num)
                    tag_dict[a]+=(num)
                
                
                except:
                    #print('no ints for this div tag')
                    #print('\n------------------')
                    pass
            #print("HERE WE GO \n\n\n")
            '''
            print(str(get_spans(a))+" Final Score:")
            try:
                #for num in tag_dict:
                #    print(num)
                print(tag_dict[0]+" - " + tag_dict[1])
            except:
            #    print("Final Score:")
                print(inner_div[18].text)
                print(inner_div[20].text)
            '''
        
        '''
        ABOVE CODE RETRIEVES COMMON INDEX FOR SCORES IN THEIR RESPECTIVE DIVS, BUT NOT ALWAYS. MODIFIED TO RETRIEVE THEM THROUGH DYNAMIC INDICES
        '''

    
    driver.close()
    return None

    

'''
TESTING SPAN TAGS
'''

def get_spans(a_tags):
    for tag in a_tags:
        sp=tag.find_all('span')
        text=""
        for span in sp:
            try:
                text=span.text
                if 'Boys' in text:
                    return(text)
            except:
                pass
    return None

    
    


'''
TESTING PULLS FROM INDIVIDUAL GAME PAGES
'''



def test_href(a_tags):
    TEST_TAG = []

    #a_tags=scroll_container.find_all('a')
    for tag in a_tags:
        try:
            link=('https://scorestream.com' + tag.get('href'))
            print(link)
            if len(TEST_TAG)<1:
                TEST_TAG.append(link)
            sp=tag.find_all('span')
            text=""
            for span in sp:
                try:
                    text=span.text
                    if 'Boys' in text:
                        pass
                        #print(text)
                except:
                    pass

        except: 
            print('no href for this \'a\' tag')


    URL_TEST = TEST_TAG[0]
    driver.get(URL_TEST)
    html=driver.page_source
    test_soup = BeautifulSoup(html, "html.parser")

    spans=test_soup.find_all('span')
    for span in spans: 
        if 'Boys' in span.text:
            print(span.text)

    driver.close()
    return None










    """ 

    OLD CODE 
    
    """
    '''
    soup = BeautifulSoup(html, "html.parser")

    #outer2 = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})
    #print(outer2)
    div_container=soup.find('div', class_="jss1")
    #"ReactVirtualized__Grid__innerScrollContainer" )
    #print(div_container)
    #outer = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})
    test=soup.find_all('div')
    #for link in test:
        #print(link.find_all("div"))
    #print(test)
    #print(outer.text)
    inner = soup.find('div', attrs={'class':'jss1'})
    #inner = soup.find('soup', attrs={'class '})
    #inner = soup.find('div', attrs={'class':"ReactVirtualized__Grid ReactVirtualized__List"})

    #inner = outer.find('div', attrs={'data-radium':'true'})
    #'aria-label':"grid", 'aria-readonly':"true", 'class':"ReactVirtualized__Grid ReactVirtualized__List", 'role':"grid", 'style':"box-sizing: border-box; direction: ltr; height: auto; position: relative; width: 796px; will-change: transform; overflow: auto;"})
        
    #'class':"ReactVirtualized__Grid__innerScrollContainer", 'role':"rowgroup", 'style':"width: auto; height: 2330px; max-width: 796px; max-height: 2330px; overflow: hidden; position: relative;"})

    #<div 'aria-label':"grid", 'aria-readonly':"true", 'class':"ReactVirtualized__Grid ReactVirtualized__List", 'role':"grid" 'style;:"box-sizing: border-box; direction: ltr; height: auto; position: relative; width: 796px; will-change: transform; overflow: auto;">
    #'class':"ReactVirtualized__Grid__innerScrollContainer"})
    #, 'role':'rowgroup','style':'width: auto; height: 2350px; max-width: 700px; max-height: 2350px; overflow: hidden; position: relative;'})
    # 'class':"ReactVirtualized__Grid__innerScrollContainer", 'role':"rowgroup", 'style':"width: auto; height: 2330px; max-width: 796px; max-height: 2330px; overflow: hidden; position: relative;"
    # Retrieve all of the anchor tags
    tbody = soup('div')
    #return inner
    return None
    #<div 'style':"overflow: visible; width: 0px;"
    #('div', attrs={'style':"height: 235px; left: 0px; position: absolute; top: 0px; width: 100%;"})
    '''
    



getFootballGames('https://scorestream.com/team/pioneer-high-school-pioneers-8385/games')


