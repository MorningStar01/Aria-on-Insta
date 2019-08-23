import os
from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rename import RenameFiles
import random

path = "C:/Users/Grim/Desktop/Aria on Insta/poze_final"
username = "pr.aria"
password = "ARIA04082019"


def Upload():
    i = 0
    a = []
    j = 0
    for files in os.listdir(path):
        image = path + "/poza_" + str(i) + ".jpg "

        with open('text2.txt', 'r+') as text:
            #s = text.readlines()

            for s in text.readlines():
                s = s.splitlines()

            text1 = s
        with client(username, password) as cli:
            cli.upload(image, text1)
        i += 1


""" 
TODO: SEE TODO.txt !!!!!!

"""

if __name__ == '__main__':
    #RenameFiles()
    Upload()
