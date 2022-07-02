import csv
import datetime

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
                cal_week = cal_date.strftime('%A')
                if judge_week(cal_week,info.week_info):
                    output_str += make_out_file_str(cal_date.month,cal_date.day,week_jp(cal_week),cal_time)
                cal_time += info.time_span

            cal_date += datetime.timedelta(days=1)
        
        fw.write(output_str.rstrip('\n'))

def judge_week(cal_week,week_info):
    if week_info.monday and cal_week == 'Monday':
        return True
    elif week_info.tuesday and cal_week == 'Tuesday':
        return True
    elif week_info.wednesday and cal_week == 'Wednesday':
        return True
    elif week_info.thursday and cal_week == 'Thursday':
        return True
    elif week_info.friday and cal_week == 'Friday':
        return True
    elif week_info.saturday and cal_week == 'Saturday':
        return True
    elif week_info.sunday and cal_week == 'Sunday':
        return True
    
def week_jp(week_eng):
    if week_eng=='Monday':
        return '月'
    elif week_eng=='Tuesday':
        return '火'
    elif week_eng=='Wednesday':
        return '水'
    elif week_eng=='Thursday':
        return '木'
    elif week_eng=='Friday':
        return '金'
    elif week_eng=='Saturday':
        return '土'
    elif week_eng=='Sunday':
        return '日'
def make_out_file_str(month,day,week,time):
    return "{month}/{day}({week}) {time}:00~\n".format(month=month, day=day, week=week, time=time)
    
def extract_csv(reader_csv):
    week_info = week()
    for i,row in enumerate(reader_csv):
        if row[0] == 'year':
            year = int(row[1]) 
        elif row[0] == 'start date':
            start_date = date(int(row[1]),int(row[2]))
        elif row[0] == 'finish date':
            finish_date = date(int(row[1]),int(row[2]))
        elif row[0] == 'monday':
            if row[1]=='1':
                week_info.monday = True
        elif row[0] == 'tuesday':
            if row[1]=='1':
                week_info.tuesday = True
        elif row[0] == 'wednesday':
            if row[1]=='1':
                week_info.wednesday = True
        elif row[0] == 'thursday':
            if row[1]=='1':
                week_info.thursday = True
        elif row[0] == 'friday':
            if row[1]=='1':
                week_info.friday = True
        elif row[0] == 'saturday':
            if row[1]=='1':
                week_info.saturday = True
        elif row[0] == 'sunday':
            if row[1]=='1':
                week_info.sunday = True
        elif row[0] == 'time start':
            time_start = int(row[1])
        elif row[0] == 'time finish':
            time_finish = int(row[1])
        elif row[0] == 'time span':
            time_span = int(row[1])
    out_info = info(year,start_date,finish_date,week_info,time_start,time_finish,time_span)
    
    return out_info
class info:
    def __init__(self,year,start_date,finish_date,week_info,time_start,time_finish,time_span):
        self.year = year
        self.start_date = start_date
        self.finish_date = finish_date
        self.week_info = week_info
        self.time_start = time_start
        self.time_finish = time_finish
        self.time_span = time_span
        self.datetime_start = datetime.datetime(year=year,month=start_date.month,day=start_date.day) + datetime.timedelta(hours=9) 
        self.datetime_finish = datetime.datetime(year=year,month=finish_date.month,day=finish_date.day) + datetime.timedelta(hours=9) 
    def print_info(self):
        print("year:",self.year)
        self.start_date.print_info()
        self.finish_date.print_info()
        self.week_info.print_info()
        print("time_start:",self.time_start)
        print("time_finish:",self.time_finish)
        print("time_span:",self.time_span)
        print("datetime_start",self.datetime_start)
        print("datetime_finish",self.datetime_finish)


class date:
    def __init__(self,month,day):
        self.month = month
        self.day = day
    def print_info(self):
        print("month:{month}, day:{day}".format(month = self.month,day = self.day))


class week:
    def __init__(self):
        self.monday = False
        self.tuesday = False
        self.wednesday = False
        self.thursday = False
        self.friday = False
        self.saturday = False
        self.sunday = False
    def print_info(self):
        print("monday   :",self.monday)
        print("tuesday  :",self.tuesday)
        print("wednesday:",self.wednesday)
        print("thursday :",self.thursday)
        print("friday   :",self.friday)
        print("saturday :",self.saturday)
        print("sunday   :",self.sunday)
        

main()
