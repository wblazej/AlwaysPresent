import pytz
from datetime import datetime
from lib.config import Config

def weekday_string(weekday):
    return Config.DAYS_OF_WEEK.get(weekday, "Invalid weekday")

def month_string(month):
    return Config.MONTHS.get(month, "Invalid month")

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