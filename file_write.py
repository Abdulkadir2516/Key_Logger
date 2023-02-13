import os

check = os.path.exists("./log.txt")

if check == False:
    open("log.txt","x", encoding="utf-8")



file = open("log.txt", "a")

file.write("deneme")

file = open("log.txt", "r")

file.read()





