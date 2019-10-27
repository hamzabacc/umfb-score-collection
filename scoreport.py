import scorescrape2
#print(scorescrape2.getScoreStream('https://scorestream.com/team/st-louis-school-crusaders-242678'))

def update_checklist(date):
    date_csv_read = open(date+"_checklist.csv", "r")
    data = date_csv_read.readlines()
    date_csv_read.close()
    date_csv = open(date+"_checklist.csv", "w")
    date_csv.write("school name, state, done?, data, scorestream url\n")
    team_info_pairs = {}
    for line in data[1:]:
        #school_is_complete = line.split('\t')[2]
        url = line.split(',')[4]
        school_name = line.split(',')[0]
        school_state = line.split(',')[1]
        info = scorescrape2.getScoreStream(url, "Varsity Football")
        info_non_csv = "***".join(info.split(','))
        #.split('\t')[3]
        try:
            final_score = info_non_csv.split("***")[3]
            #if final_score.startswith("L ") or final_score.startwith("W "):
            if "L " in final_score or "W " in final_score:
                date_csv.write(",".join([school_name,school_state,'Y',info_non_csv,url]))
            else:
                date_csv.write(",".join([school_name,school_state,'N',info_non_csv,url]))
        except:
            date_csv.write(",".join([school_name, school_state, 'N', info_non_csv, url]))
    date_csv.close()
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

#date_check
print(update_checklist("october 26"))