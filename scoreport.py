import scorescrape2
print(scorescrape2.getScoreStream('https://scorestream.com/team/pioneer-high-school-pioneers-8385'))

def update_checklist(date):
    date_csv_read = open(date+"_checklist.csv", "r")
    data = date_csv_read.readlines()
    date_csv_read.close()
    date_csv = open(date+"_checklist.csv", "w")
    date_csv.write("school name, state, done?, data, scorestream url\n")
    team_info_pairs = {}
    for line in data[1:]:
        school_is_complete = line[2]
        if school_is_complete=="Y":
            date_csv.write(line)
            continue
        url = line[4][:-2]
        return url
        info = scorescrape2.getScoreStream(url)
        final_score = info.split(",")[4]
        if final_score.startswith("L ") or final_score.startwith("W "):
            date_csv.write([line[0],line[1],'Y',info,url].join(','))
    return None



def date_checklist_creator(date):
    '''try:
        date_csv = open(date+"_checklist.csv", "r")
    except:'''
    input_file = open("player_data_input.csv", "r")
    checklist = open(date+"_checklist.csv", "w")
    checklist.write("school name, state, done?, data, scorestream url\n")
    for line in input_file.readlines()[1:]:
        line_info_list = line.split(',')
        school_name = scorescrape2.getFullSchoolName(line_info_list[6])
        school_state = line_info_list[4]
        school_url = line_info_list[6]
        checklist.write(school_name+","+school_state+","+"N,,"+school_url)
    input_file.close()
    checklist.close()
    '''date_csv_contents = date_csv.readlines()
        date_csv_len = len(date_csv_contents)
        if date_csv_len>0:
            pass
        else:'''
    return None


#print(date_checklist_creator("october 26"))