from rich import print
from faker import Faker
from datetime import datetime,timedelta,date
from collections import defaultdict
import locale 
from  random import Random
import calendar


def parse_data(bd: date | datetime | str) -> date | None:
    user_bd = None
    try:
        if isinstance(bd, datetime) :
            user_bd = bd.date()
        elif isinstance(bd, date):
            user_bd = bd
        elif isinstance(bd, str):
            if len(bd.split('-')) == 3:
                user_bd = datetime.strptime(bd, "%Y-%m-%d").date()
            elif len(bd.split('.')) == 3:
                user_bd = datetime.strptime(bd, "%d.%m.%Y").date()
            else:
                user_bd = date.fromisoformat(bd)
    except  ValueError as e:
        print("format of date undefined", bd, e)
        ...

    return user_bd

def print_users(weekdays: dict) -> None:
    for weekday, users in sorted(weekdays.items()):
        if isinstance(weekday, date) or isinstance(weekday, datetime):
            weekday = weekday.strftime("%A, %x")
        userlist = [user['name'] for user in users]
        print(f"{weekday} : {userlist}")
        



def get_birthdays_per_week(users: list | tuple) -> list:

    result = defaultdict(list)
    current_datetime = datetime.now().date()
    curr_week = current_datetime.weekday()
    start_weeks_interval = timedelta(days=5-curr_week)
    end_weeks_interval = timedelta(days=6)
    next_monday = current_datetime + timedelta(days=7-curr_week)
    start_week = current_datetime + start_weeks_interval
    end_week = start_week + end_weeks_interval

    for user in users:
        user_bd = parse_data(user["birthday"])
        if not user_bd :
            print(f"format of date undefined, skip, user {user['name']}")
            continue
        user_bd_this_year = user_bd.replace(year=current_datetime.year)
        if  start_week <= user_bd_this_year <= end_week:
            user_week = user_bd_this_year.weekday()
            user_bd_day  = calendar.day_name[user_week]
            if user_week >= 5:
                user['weekend'] = user_bd_day
                day = next_monday
            else:
                day = user_bd_this_year
            result[day].append(user)
    #result_map = {calendar.day_name[k]: v for k, v in sorted(result.items())}

    return result



#MAIN

if __name__ == "__main__":

    lang = ""
    lang = locale.getdefaultlocale()[0]
    locale.setlocale(locale.LC_ALL, lang) 


    f = Faker(lang)
    #current_date = datetime.now().date()
    current_date = datetime.now().date()
    
#                "birthday": (current_date + timedelta(days=Random().randrange(1,30))).strftime("%Y-%m-%d")
    users = ( { "name": f.name() ,  
                "birthday": (current_date + timedelta(days=Random().randrange(1, 30))).strftime("%d.%m.%Y")
            } for i in range(50) )

    #print(users)
    birthday_result = get_birthdays_per_week(users)
    print_users(birthday_result)


"""
Monday: Bill, Jill
Friday: Kim, Jan
"""