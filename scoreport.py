import scorescrape2
#print(scorescrape2.getFullSchoolName('https://scorestream.com/team/pioneer-high-school-pioneers-8385'))

def d1(date):
    date_csv = open(date+"_checklist.csv", "r")
    for line in date_csv.readlines()[1:]:
        pass
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


print(date_checklist_creator("october 26"))