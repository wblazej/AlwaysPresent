from lib.format_date import FormatDate

class Logging:
    @staticmethod
    def error(content):
        print(f"\033[1m\033[91mERROR\033[0m {content} | {FormatDate.get_formated_datetime()}")

    @staticmethod
    def info(content):
        print(f"\033[94m\033[1mINFO\033[0m {content} | {FormatDate.get_formated_datetime()}")