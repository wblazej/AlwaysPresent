import pytz
from datetime import datetime

def weekday_string(weekday):
    switcher = {
        0: "poniedziałek",
        1: "wtorek",
        2: "środa",
        3: "czwartek",
        4: "piątek",
        5: "sobota",
        6: "niedziela"
    }

    return switcher.get(weekday, "Invalid weekday")

def month_string(month):
    switcher = {
        1: "Styczeń",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecień",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpień",
        9: "Wrzesień",
        10: "Październik",
        11: "Listopad",
        12: "Grudzień"
    }

    return switcher.get(month, "Invalid month")

def get_formated_warsaw_datetime():
    tz = pytz.timezone('Europe/Warsaw')
    dt = datetime.now(tz)

    day = dt.day
    month = month_string(dt.month)
    week_day = weekday_string(dt.weekday())

    hour = dt.hour
    minute = dt.minute

    if day < 10:
        day = f'0{day}'
    if hour < 10:
        hour = f'0{hour}'
    if minute < 10:
        minute = f'0{minute}'

    return f'{day} {month} ({week_day}) {hour}:{minute}'