from rich import print
from faker import Faker
from datetime import datetime,timedelta
from collections import defaultdict
import locale 
from  random import Random
import calendar


def get_birthdays_per_week(users):

    result = defaultdict(list)
    current_datetime = datetime.now()
    curr_week = current_datetime.weekday()
    start_weeks_interval = timedelta(days=5-curr_week)
    end_weeks_interval = timedelta(days=6)
    start_week = current_datetime + start_weeks_interval
    end_week = start_week + end_weeks_interval

    # print(current_datetime.date())
    # print(start_week.date())
    # print(end_week.date())

    for user in users:
        bd = user["birthday"]
        user_bd = datetime.strptime(bd, "%Y-%m-%d")
        #print(user_bd,user_bd_day)
        user_bd_this_year = datetime(current_datetime.year, user_bd.month, user_bd.day)
        #print(f"user_bd_this_year: {user_bd_this_year}")
        if  start_week <= user_bd_this_year <= end_week:
            #print(f"user_bd_this_year weekday: {user_bd_this_year.weekday()}")
            user_week = user_bd_this_year.weekday()
            #user_bd_day = user_bd.strftime("%A")
            user_bd_day  = calendar.day_name[user_week]
            if user_week > 5:
                #print(f"Weekend: {user_bd_day} {user['name']}")
                user['weekend'] = user_bd_day
                user_week = 0
            day = user_week
            #name = user["name"]
            result[day].append(user)
    result_map = {calendar.day_name[k]: v for k, v in sorted(result.items())}

    return result_map



#MAIN

if __name__ == "__main__":

    lang = locale.getdefaultlocale()[0]
    locale.setlocale(locale.LC_ALL, lang) 


    f = Faker(lang)
    current_date = datetime.now()

    users = [ { "name": f.name() ,  
                "birthday": (current_date + timedelta(days=Random().randrange(1,30))).strftime("%Y-%m-%d")
            } for i in range(50) ]

    print(users)

    print(get_birthdays_per_week(users))


"""
Monday: Bill, Jill
Friday: Kim, Jan
"""