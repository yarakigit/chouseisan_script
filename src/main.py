import csv
import datetime

week_dict = {
     0:'Monday',
     1:'Tuesday',
     2:'Wednesday',
     3:'Thursday',
     4:'Friday',
     5:'Saturday',
     6:'Sunday'
}

def main():
    in_file_name = '../setting.csv'
    out_file_name = '../output.txt'
    with open(in_file_name, mode='r') as fr, open(out_file_name, mode='w') as fw:
        reader_csv = csv.reader(fr)
        info=extract_csv(reader_csv=reader_csv)
        info.print_info()
        cal_date = info.datetime_start
        output_str = ''
        while (cal_date - info.datetime_finish).days <= 0:
            cal_time = info.time_start
            while info.time_finish>=cal_time:
                exclusion_date_flag = False
                for exclusion_date in info.exclusion_date_list:
                    if exclusion_date.month==cal_date.month and exclusion_date.day==cal_date.day: 
                        exclusion_date_flag = True
                exclusion_time_flag = False
                for exclusion_time in info.exclusion_time_list:
                    if exclusion_time==cal_time:
                        exclusion_time_flag = True
                if not (exclusion_date_flag or exclusion_time_flag):
                    cal_week = cal_date.strftime('%A')
                    if judge_week(cal_week,info.week_info):
                        output_str += make_out_file_str(cal_date.month,cal_date.day,week_jp(cal_week),cal_time)
                cal_time += info.time_span
            cal_date += datetime.timedelta(days=1)
        fw.write(output_str.rstrip('\n'))

def judge_week(cal_week,week_info):
    if week_info.Monday and cal_week == week_dict[0]:
        return True
    elif week_info.Tuesday and cal_week == week_dict[1]:
        return True
    elif week_info.Wednesday and cal_week == week_dict[2]:
        return True
    elif week_info.Thursday and cal_week == week_dict[3]:
        return True
    elif week_info.Friday and cal_week == week_dict[4]:
        return True
    elif week_info.Saturday and cal_week == week_dict[5]:
        return True
    elif week_info.Sunday and cal_week == week_dict[6]:
        return True
    
def week_jp(week_eng):
    if week_eng==week_dict[0]:
        return '月'
    elif week_eng==week_dict[1]:
        return '火'
    elif week_eng==week_dict[2]:
        return '水'
    elif week_eng==week_dict[3]:
        return '木'
    elif week_eng==week_dict[4]:
        return '金'
    elif week_eng==week_dict[5]:
        return '土'
    elif week_eng==week_dict[6]:
        return '日'
def make_out_file_str(month,day,week,time):
    return "{month}/{day}({week}) {time}:00~\n".format(month=month, day=day, week=week, time=time)
    
def extract_csv(reader_csv):
    week_info = week()
    exclusion_date_list = []
    exclusion_time_list = []
    for i,row in enumerate(reader_csv):
        if len(row) == 0:
            break
        elif row[0] == 'year':
            year = int(row[1]) 
        elif row[0] == 'start date':
            start_date = date(int(row[1]),int(row[2]))
        elif row[0] == 'finish date':
            finish_date = date(int(row[1]),int(row[2]))
        elif row[0] == week_dict[0]:
            if row[1]=='1':
                week_info.Monday = True
        elif row[0] == week_dict[1]:
            if row[1]=='1':
                week_info.Tuesday = True
        elif row[0] == week_dict[2]:
            if row[1]=='1':
                week_info.Wednesday = True
        elif row[0] == week_dict[3]:
            if row[1]=='1':
                week_info.Thursday = True
        elif row[0] == week_dict[4]:
            if row[1]=='1':
                week_info.Friday = True
        elif row[0] == week_dict[5]:
            if row[1]=='1':
                week_info.Saturday = True
        elif row[0] == week_dict[6]:
            if row[1]=='1':
                week_info.Sunday = True
        elif row[0] == 'time start':
            time_start = int(row[1])
        elif row[0] == 'time finish':
            time_finish = int(row[1])
        elif row[0] == 'time span':
            time_span = int(row[1])
        elif row[0] == 'exclusion date':
            if not row[1] == 'None':
                exclusion_date_list.append(date(int(row[1]),int(row[2])))
        elif row[0] == 'exclusion time':
            if not row[1] == 'None':
                exclusion_time_list.append(int(row[1]))
    out_info = info(year,start_date,finish_date,week_info,time_start,time_finish,time_span,exclusion_date_list,exclusion_time_list)
    
    return out_info
class info:
    def __init__(self,year,start_date,finish_date,week_info,time_start,time_finish,time_span,exclusion_date_list,exclusion_time_list):
        self.year = year
        self.start_date = start_date
        self.finish_date = finish_date
        self.week_info = week_info
        self.time_start = time_start
        self.time_finish = time_finish
        self.time_span = time_span
        self.datetime_start = datetime.datetime(year=year,month=start_date.month,day=start_date.day) + datetime.timedelta(hours=9) 
        self.datetime_finish = datetime.datetime(year=year,month=finish_date.month,day=finish_date.day) + datetime.timedelta(hours=9) 
        self.exclusion_date_list = exclusion_date_list
        self.exclusion_time_list = exclusion_time_list
    def print_info(self):
        print("year:",self.year)
        print("start_date : ",end='')
        self.start_date.print_info()
        print("finish_date : ",end='')
        self.finish_date.print_info()
        self.week_info.print_info()
        print("time_start:",self.time_start)
        print("time_finish:",self.time_finish)
        print("time_span:",self.time_span)
        print("datetime_start",self.datetime_start)
        print("datetime_finish",self.datetime_finish)
        for exclusion_date in self.exclusion_date_list:
            print("exclusion_date : ",end='')
            exclusion_date.print_info()
        for exclusion_time in self.exclusion_time_list:
            print("exclusion_time : ",end='')
            print(exclusion_time)
        
class date:
    def __init__(self,month,day):
        self.month = month
        self.day = day
    def print_info(self):
        print("month:{month}, day:{day}".format(month = self.month,day = self.day))


class week:
    def __init__(self):
        self.Monday = False
        self.Tuesday = False
        self.Wednesday = False
        self.Thursday = False
        self.Friday = False
        self.Saturday = False
        self.Sunday = False
    def print_info(self):
        print('{week:<9}: {week_en}'.format(week=week_dict[0],week_en=self.Monday))
        print('{week:<9}: {week_en}'.format(week=week_dict[1],week_en=self.Tuesday))
        print('{week:<9}: {week_en}'.format(week=week_dict[2],week_en=self.Wednesday))
        print('{week:<9}: {week_en}'.format(week=week_dict[3],week_en=self.Thursday))
        print('{week:<9}: {week_en}'.format(week=week_dict[4],week_en=self.Friday))
        print('{week:<9}: {week_en}'.format(week=week_dict[5],week_en=self.Saturday))
        print('{week:<9}: {week_en}'.format(week=week_dict[6],week_en=self.Sunday))
        
        

main()