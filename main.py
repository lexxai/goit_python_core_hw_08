from rich import print
from faker import Faker
from datetime import datetime,timedelta
import locale 







from collections import defaultdict

def get_birthdays_per_week(users):
    result = defaultdict(list)
    current_datetime = datetime.now()
    curr_week = current_datetime.weekday()
    start_weeks_interval = timedelta(days=7-curr_week)
    end_weeks_interval = timedelta(days=6)
    start_week = current_datetime + start_weeks_interval
    end_week = start_week + end_weeks_interval

    print(current_datetime.date())
    print(start_week.date())
    print(end_week.date())

    for user in users:
        bd = user["birthday"]
        user_bd = datetime.strptime(bd, "%Y-%m-%d")
        
        user_bd_day = user_bd.strftime("%A")
        print(user_bd,user_bd_day)
        user_bd_this_year = datetime(current_datetime.year, user_bd.month, user_bd.day)
        print(f"user_bd_this_year: {user_bd_this_year}")
        if  start_week <= user_bd_this_year <= end_week:
             print(f"user_bd_this_year weekday: {user_bd_this_year.weekday()}")


        search_week = start_week
        one_day = timedelta(days=1)
        while search_week < end_week:
            print(f"search_week: {search_week}")
            search_week += one_day

        if True:
            day = "Mon"
            name = user["name"]
            result[day].append(name)
        #print(user["birthday"])
    return result


lang = locale.getdefaultlocale()[0]
@locale.setlocale(locale.LC_ALL, lang) 


f = Faker(lang)
current_date = datetime.now()

users = ( { "name": f.name() ,  
            "birthday": current_date + timedelta(days=i) 
          } for i in range(15) )
print(users)

#print(get_birthdays_per_week(users))


"""
Monday: Bill, Jill
Friday: Kim, Jan
"""