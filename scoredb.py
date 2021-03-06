
import sqlite3
import scorescrape2

conn = sqlite3.connect('Scores.sqlite')
cur = conn.cursor()
cur.execute('drop table if exists Schools')
cur.execute('create table Schools(name text, scorestreamURL text)')


f = open('DB_TEST_2020PROSPECT_27AUGUST2019.csv', 'r')
lines = f.readlines()
count = 0
f.close()


for line in lines:
    if count==0:
        count+=1
    else:
        name = line.split(',')[0]
        if (line.split(',')[1]!='\n'):
            url = line.split(',')[1]
            command = 'insert into Schools (name, scorestreamURL) values (?,?)'
            values = (name, url)
            cur.execute(command, values)

        else: pass

conn.commit()


f=open('newtestdoc2.csv','w')

(cur.execute('select * from Schools'))
count=0
f.write('team, state, opponent, score, date\n')
for row in (cur.fetchall()):
    if(len(row[1])==0):
        f.write("no scorestream link for this school")
    else:
        f.write(scorescrape2.getScoreStream(row[1]+'/games','Boys Varsity Football')+"\n")
f.close()

