
import sqlite3
import scorescrape2

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


f=open('newtestdoc2.csv','w')
#f.write(scorescrape.getScoreStream)

#f=open('TEST_BASEBALL_SCORES_19AUGUST2019.csv','w')
(cur.execute('select * from Schools'))
count=0
f.write('team, state, opponent, score, date\n')
for row in (cur.fetchall()):
    if(len(row[1])==0):
        f.write("no scorestream link for this school")
    else:
        f.write(scorescrape2.getScoreStream(row[1]+'/games','Boys Varsity')+"\n")
f.close()
'''

    #if count>0:
    #    break
    count+=1
    #print(row[1])
    #print(scorescrape.getScoreStream(row[1]+'/games','Boys Varsity Baseball'))
    
    schoolData=[row[0],row[1][0:len(row[1])-2]]
    score = scorescrape.getScoreStream(row[1]+'/games','Boys Varsity Baseball')
    try: 
        schoolData.append(score[0][0:len(score)-2])
    except:
        schoolData.append(',,,,,NO RECENT SCORE DATA AVAILABLE FOR THIS SCHOOL FOR THE SELECTED SPORT')
    #print(schoolData)
    schoolData.append('\n')
    f.write(','.join(schoolData))
f.close()'''



'''NEXT STEPS:
- FORMAT MAXPREPS OUTPUT TO MATCH SCORESCRAPE OUTPUT
- ADD CODE TO MAKE DATABASE ENTRY FOR MAXPREPS SCORES/OUTPUTS
- CHANGE DATABASE COLUMN TITLES TO REFLECT SCORESTREAM-SPECIFIC DATA TO BE COMP'D WITH MAXPREPS DATA




** MODIFY THE GETFOOTBALLGAMES METHOD TO ACCEPT PARAMETER OF WHICH SPORT TO RETRIEVE SCORE OF



$$ ADD DATE EXTRACTION WITH SCORES AND METHOD TO CONVERT DATE SO IT ONLY RETRIEVES WITHIN LIMITED DATE PARAMETER.
THIS WILL ALLOW SEPARATE SQL SHEET FOR EACH WEEK OF THE FOOTBALL SEASON
'''
