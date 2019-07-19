import sqlite3

conn = sqlite3.connect('Scores.sqlite')
cur = conn.cursor()
cur.execute('drop table if exists Schools')
cur.execute('create table Schools(name text, scorestreamURL text)')


f = open('DB_TEST_2020PROSPECT_18JULY2019.csv', 'r')
lines = f.readlines()
count = 0


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
            print(values)
            cur.execute(command, values)

        else: pass


