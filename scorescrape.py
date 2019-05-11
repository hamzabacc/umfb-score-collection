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

#path=r'C:\\Users\\Hamza\\Documents\\Football'
#driver = webdriver.Chrome(executable_path = path)


def getFootballGames(url):
    path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    #driver = webdriver.Chrome(executable_path=r"C:\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)

    #print(driver)
    #print(driver.find_element_by_link_text('football'))
    #sys.exit()
    #url = input('Enter - ')
    #html = urlopen(url).read()
    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)
    #info= soup.find_all('div', class_="ReactVirtualized__Grid__innerScrollContainer")
    #print(info)
    #print(soup.get_text())
    b=soup.find('body')
    #print(b)
    test_outer = soup.find('div', attrs={'id':"react-root",'class':"scorestream_ui"})
    #print(outer)
    #time.sleep(10)




    outer=soup.find('div', attrs={'class':'rmq-1c61845d'})
    #print(outer)  
    scroll_container=soup.find('div', attrs={'class':'ReactVirtualized__Grid__innerScrollContainer'})
    print(scroll_container)

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
    return inner
    val=0
    for tag in tbody:
        val=val+int(tag.string)
        
    return val

print(getFootballGames('https://scorestream.com/team/pioneer-high-school-pioneers-8385/games'))

#<div 'style':"overflow: visible; width: 0px;"

