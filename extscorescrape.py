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
import datescratch


def getExtScoreStream(url, sportKey=""):

    global GAMES
    GAMES=[]
    #FALL = True

    path=r'C:\Users\Hamza\Documents\Football\chromedriver.exe'
    global driver 
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)

    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    '''
    CODE TO OBTAIN SCROLL CONTAINER + TAGS
    '''

    span_city_state=soup.find('span', attrs={'itemprop':'address'})
    city_state=span_city_state.text
    state=city_state[len(city_state)-2:]

    scroll=True
    
    while scroll: 
        #driver.get(url)
        count=0
        if count==0:
            pass
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        html=driver.page_source
        soup = BeautifulSoup(html, "html.parser")
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

        for a in a_tags:
            spans=a.find_all('span')
            date=(spans[7].text)
            print (date)

            '''
            for span in spans:
                if (sportKey in span.text):
                    football_game=True
                sport=(spans[4].text)
            print(sport)'''

            


        TEAM_NAME=str(soup.find('h1').text)



        #a_index=0
        football_game=False
        for a in a_tags:
            RESULT=""
            cont=False
            spans=a.find_all('span')
            for span in spans:
                if (sportKey in span.text):
                    football_game=True
                sport=(spans[4].text)
                #print(a_index)
                #a_index+=1
            print(sport)
            div1=a.find('div')
            div2=div1.find('div')
            #a_index+=1
            if (football_game):
                break

            #print(football_game)
            cancelled=False
            inners= div2.find_all('div',attrs={'style':"font-size: 48px; display: flex; position: relative; flex-direction: column;"})
            try: 
                if ("Cancelled" in inners[0].find('div').text):
                    cancelled=True
            except: pass
            

            ints=[]
            #final = False
            for tag in inners[0].find_all('div'):
                try:
                    ints.append(int(tag.text))
                except:
                    pass
                if(tag.text==('Final')):
                        final=True
            
            away_team=(spans[0].text+" "+spans[1].text)
            home_team=(spans[2].text+" "+spans[3].text)

            #two_scores=True
            date=(spans[7].text)
            #return date
            '''if ("\'18" in date and "\'19" not in date):
                driver.close()
                return TEAM_NAME+","+state+','+"N/A"+",no recent football scores available,"'''

            if cancelled:
                driver.close()
                if(TEAM_NAME==(away_team)):
                    RESULT = TEAM_NAME+','+state+','+'@'+home_team+","+'Cancelled,'+datescratch.date_format(date)+','
                    GAMES.append(RESULT.split(','))
                    cont=True
                else: 
                    RESULT= TEAM_NAME+','+state+','+'vs. '+away_team+','+'Cancelled,'+datescratch.date_format(date)+','
                    GAMES.append(RESULT.split(','))
                    cont=True
            



            '''if 'Last' not in date and 'Yesterday' not in date and 'Today' not in date and football_game:
                driver.close()
                return TEAM_NAME+","+state+','+"N/A"+",most recent score isn't from this week"'''


            if(len(ints)>2):
                two_scores=False
            else:
                away_score=ints[0]
                home_score=ints[1]
            
            print(away_score)
            print(home_score)

            

            #RESULT = ""
            outcome= ""
            opponent=""
            if TEAM_NAME==(away_team):
                opponent="@ " + home_team
                if(away_score>home_score):
                    outcome='W '+str(away_score)+"-"+str(home_score)
                else: 
                    if(home_score>away_score):
                        outcome='L '+str(home_score)+"-"+str(away_score)
                RESULT=away_team+','+state+','+'@ '+str(home_team)+','+outcome+','+datescratch.date_format(date)
            else:
                if TEAM_NAME==(home_team):
                    opponent="vs. " + away_team
                    if(away_score>home_score):
                        outcome='L '+str(away_score)+"-"+str(home_score)
                    else: 
                        if(home_score>away_score):
                            outcome='W '+str(home_score)+"-"+str(away_score)
                RESULT=home_team+','+state+','+'vs. '+str(away_team)+','+outcome+','+datescratch.date_format(date)
            #driver.close()
            #print(football_game)
            ''''if not football_game:
                driver.close()
                return TEAM_NAME+","+state+','+"N/A"+",no recent football scores available,"
            if not two_scores:
                driver.close()
                return(TEAM_NAME+","+state+','+opponent+",more than two score numbers pulled. check manually,")
            if not final:
                driver.close()
                return(TEAM_NAME+","+state+','+opponent+",score available is not a final score,"+datescratch.date_format(date))'''
            
            
            #return RESULT
            GAMES.append(RESULT.split(','))

            if 'Jul' in date or 'Jun' in date or 'May' in date or 'Apr' in date or 'Mar' in date or 'Feb' in date or 'Jan' in date or '\'18' in date:
                scroll=False
        '''if 'Jul' in date or 'Jun' in date or 'May' in date or 'April' in date or '\'18' in date:
            driver.close()
            #driver.quit()
            break
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        html=driver.page_source
        soup = BeautifulSoup(html, "html.parser")'''
    
    try:
        driver.close()
    except:
        pass
    #driver.quit()
    return GAMES

print(getExtScoreStream('https://scorestream.com/team/st-louis-school-crusaders-242678/games','Boys Varsity Football'))
