from datetime import datetime

def get_time():
    return datetime.now().strftime("%A, %d %B %Y %H:%M:%S")

class Logging:
    @staticmethod
    def error(content):
        print(f"\033[1m\033[91mERROR\033[0m {content} | {get_time()}")

    @staticmethod
    def info(content):
        print(f"\033[94m\033[1mINFO\033[0m {content} | {get_time()}")