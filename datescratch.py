# from datetime import date
# import datetime
# import math
# from pytz import timezone


from datetime import datetime, timedelta

'2015-05-26'
'''

from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
'''

def date_format(date):
    days={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    weekday=0
    for key in days:
        if key in date:
            weekday=int(days[key])
            break
        
    
    return datetime.strftime(datetime.now() - timedelta(weekday), '%m-%d')
    #date.today()
    
    '''est = timezone('EST')
    date = str(datetime.now(est)).split()[0].split("-")
    date="_".join(date)
    return date
    
    est = timezone('EST')
    return datetime.now(est)


    #weekday_int=(datetime.datetime.today().weekday())
    #days_ago=math.abs(weekday_int-gameday_int)'''

print(date_format("Last Thursday at 7:00 PM"))


'''

difference in days  = curr_num - date_num
differenc in seconds = 3*3600*24
date_words=date.split()
time =""
for word in date_words:
    if ':' in word:
        time=word
hours = int(time.split(':')[0])
minutes = int(time.split(':')[1])
if date_words[-1]=='PM':
    hours+=12
difference in seconds -=hours*3600
difference in seconds -=minutes*60



'''