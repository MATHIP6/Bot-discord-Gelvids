from random import *

def randomNitro():
    nombre = ["a", "b", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "n", 
    "A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N", 
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    b = ""
    for i in range(16):
        n = choice(nombre)
        b =  b + n
    url = "https://discord.gift/" + b
    return url