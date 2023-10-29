from random import *

def word(mot):
    char = ""
    charr = []
    a = []
    moot = mot
    i = 0
    for mots in moot:
        charr.append(mots)
    while charr != a:
        c = randint(0, (len(charr) - 1))
        char = char + charr[c]
        charr.remove(charr[c])
    return char

