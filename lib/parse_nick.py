import re
from datetime import datetime
import bisect

FOLDER = "lib/parse_nick_data/"
names = open(f"{FOLDER}names", "r").read().split('\n')
surnames = open(f"{FOLDER}surnames", "r").read().split('\n')
disallowed_words = open(f"{FOLDER}disallowed_words").read().split('\n')

def parse_nick(nick: str):
    nick = re.sub("[0-9]\.? ?", "", nick)
    words = nick.split()

    to_pop = []
    for w in range(len(words)):
        if words[w].upper() in disallowed_words:
            to_pop.append(w)
    for tp in to_pop:
        words.pop(tp)

    name = ''
    surname = ''
    for w in range(len(words)):
        index = bisect.bisect_left(names, words[w].upper())
        if names[index] == words[w].upper():
            name = words[w]
            words.pop(w)
            break

    for w in range(len(words)):
        index = bisect.bisect_left(surnames, words[w].upper())
        if surnames[index] == words[w].upper():
            surname = words[w]

    return name, surname