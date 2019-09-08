import sqlite3
import scorescrape2

conn = sqlite3.connect('Scores.sqlite')
cur = conn.cursor()
cur.execute('drop table if exists Scores')
cur.execute('create table Scores(school text, ss_school text, scorestreamURL text)')
cur.execute('drop table if exists Players')
cur.execute('create table Players(first_name text, last_name text, pos text, school text, state text)')


f = open('DB_TEST_2020PROSPECT_27AUGUST2019.csv', 'r')
lines = f.readlines()
count = 0
f.close()


for line in lines:
    if count==0:
        count+=1
    else:
        data=line.split(',')
        first_name = data[0]
        last_name = data[1]
        position = data[2]
        school_name = data[3]
        school_state = data[4]
        command = 'insert into Scores (first_name, last_name, pos, school, state) values (?,?,?,?,?)'
        vals = (first_name,last_name,position,school_name,school_state)
        cur.execute(command,vals)
        
        
        
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

