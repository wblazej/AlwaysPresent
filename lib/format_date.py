import pytz
from datetime import datetime

# libs
from lib.config import Config
# from lib.logging import Logging

class FormatDate:
    @staticmethod
    def weekday_string(weekday):
        return Config.DAYS_OF_WEEK.get(weekday, "Invalid weekday")

    @staticmethod
    def month_string(month):
        return Config.MONTHS.get(month, "Invalid month")

    @staticmethod
    def get_current_datetime():
        try:
            tz = pytz.timezone(Config.TIMEZONE)
            return datetime.now(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            # Logging.error("Incorrect timezone has been provided in config file")
            pass

    @staticmethod
    def get_formated_datetime(dt: datetime = None):
        if not dt:
            dt = FormatDate.get_current_datetime()

        day = dt.day
        month = FormatDate.month_string(dt.month)
        week_day = FormatDate.weekday_string(dt.weekday())

        hour = dt.hour
        minute = dt.minute

        if day < 10:
            day = f'0{day}'
        if hour < 10:
            hour = f'0{hour}'
        if minute < 10:
            minute = f'0{minute}'

        return f'{week_day}, {day} {month} {hour}:{minute}'

    @staticmethod
    def get_formated_time(dt: datetime = None):
        if not dt:
            dt = FormatDate.get_current_datetime()

        hour = dt.hour
        minute = dt.minute
        if hour < 10: hour = f"0{hour}"
        if minute < 10: minute = f"0{minute}"

        return f'{hour}:{minute}'