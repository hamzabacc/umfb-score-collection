import sqlite3
import scorescrape

conn = sqlite3.connect('Scores.sqlite')
cur = conn.cursor()
cur.execute('drop table if exists Schools')
cur.execute('create table Schools(name text, scorestreamURL text)')


f = open('DB_TEST_2020PROSPECT_18JULY2019.csv', 'r')
lines = f.readlines()
count = 0
f.close()


for line in lines:
    #print(line)
    if count==0:
        count+=1
    else:
        name = line.split(',')[0]
        if (line.split(',')[1]!='\n'):
            url = line.split(',')[1]
            command = 'insert into Schools (name, scorestreamURL) values (?,?)'
            values = (name, url)
            #print(values)
            cur.execute(command, values)

        else: pass

conn.commit()


f=open('TEST_BASEBALL_SCORES_19JULY2019.csv','w')
(cur.execute('select * from Schools'))
count=0
for row in (cur.fetchall()):
    if count>0:
        break
    count+=1
    print(row[1])
    #print(scorescrape.getFootballGames(row[1]+'/games','Boys Varsity Baseball'))
    schoolData=[row[0],row[1],scorescrape.getFootballGames(row[1]+'/games','Boys Varsity Baseball')]
    print(schoolData)
    #f.write(','.join(schoolData))




'''TOMORROW:
CREATE THIRD FILE FOR TEST SCORE RETRIEVAL:
- IMPORT SCORESCRAPE FILE
- RETRIEVE EACH SCHOOL'S NAME AND URL
- TEST MOST RECENT SCORE RETRIEVAL FOR EACH ONE FOR VARIOUS SPORTS

** MODIFY THE GETFOOTBALLGAMES METHOD TO ACCEPT PARAMETER OF WHICH SPORT TO RETRIEVE SCORE OF



$$ ADD DATE EXTRACTION WITH SCORES AND METHOD TO CONVERT DATE SO IT ONLY RETRIEVES WITHIN LIMITED DATE PARAMETER.
THIS WILL ALLOW SEPARATE SQL SHEET FOR EACH WEEK OF THE FOOTBALL SEASON
'''
