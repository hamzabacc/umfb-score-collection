import sqlite3

conn = sqlite3.connect('Scores.sqlite')
cur = conn.cursor



f = file.open('DB_TEST_2020PROSPECT_18JULY2019.csv', 'r')
lines = f.readlines()
count = 0


for line in lines:
    if count==0:
        count+=1
        continue
    else:
        name = line.split()[0]
        url = line.split()[1]


