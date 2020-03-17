import os
from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rename import RenameFiles
import random
import textwrap

path = "C:/Users/Grim/Desktop/Aria on Insta/__pycache__/poze ish sortate"
username = "***********"
password = "***********"

#create lists to store quotes and authors in
lines = [line.rstrip() for line in open('quotes.csv')]
authors = [author.rstrip() for author in open('authors.csv')]

for val in enumerate(lines):

    #print(val)
    para = textwrap.wrap(val)
    for line in para:
        s = textwrap.fill(line, width=70)
        print(s)


def Upload():
    i = 0
    for files in os.listdir(path):
        image = path + "/poza_" + str(i) + ".jpg "

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
