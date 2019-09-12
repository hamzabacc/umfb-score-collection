import sqlite3
import scorescrape2
conn = sqlite3.connect('Scores.sqlite')

def scoredb():
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute('drop table if exists Scores')
    cur.execute('create table Scores(school text, ss_school text, scorestreamURL text)')
    cur.execute('drop table if exists Players')
    cur.execute('create table Players(first_name text, last_name text, pos text, school text, state text)')


    f = open('DB_2020PROSPECTS.csv', 'r')
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
            command = 'insert into Players (first_name, last_name, pos, school, state) values (?,?,?,?,?)'
            vals = (first_name,last_name,position,school_name,school_state)
            cur.execute(command,vals)
            
            
            '''
            if (line.split(',')[1]!='\n'):
                url = line.split(',')[1]
                command = 'insert into Schools (name, scorestreamURL) values (?,?)'
                values = (name, url)
                cur.execute(command, values)

            else: pass'''

    conn.commit()



    f=open('newtestdoc4.csv','w')

    (cur.execute('select * from Players'))
    count=0
    f.write('first name, last name, position, team, state, opponent, score, date\n')
    for row in (cur.fetchall()):
        cur2.execute('select * from Schools')
        url = cur2.fetchall()[count][1]
        count+=1
        f.write(row[0]+','+row[1]+','+row[2]+','+scorescrape2.getScoreStream(url+'/games','Boys Varsity Football')+"\n")
    f.close()

    '''ABOVE: WRITING SCORES TO THE CSV AFTER ACQUIRING SCHOOL URL FROM SCHOOLS DB'''

def databasecopy(week, last=""):
    f = open('newtestdoc4.csv','r')
    cur3=conn.cursor()
    cur3.execute('drop table if exists ' + week)
    cur3.execute('create table '+week+'(team,state,opponent,score,date)')
    for row in f.readlines()[1:]:
        team = row.split(',')[3]
        states = row.split(',')[4]
        opponent = row.split(',')[5]
        score = row.split(',')[6]
        try: date = row.split(',')[7]
        except: date = ""
        scores_command='Insert into ' + week + ' (team, state, opponent, score, date) values (?,?,?,?,?)'
        scores_values=(team,states,opponent,score,date)
        cur3.execute(scores_command,scores_values)
    f.close()
    conn.commit()


databasecopy("September7th2019")

