import os
from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rename import RenameFiles
import random
import time
import random

path = "C:/Users/Grim/Desktop/Aria on Insta/final_q"
username = "username"
password = "password"

for x in range(1):
    a = random.uniform(1.0, 9.2) * 3600
    print(a)


def Upload():
    i = 0
    for files in os.listdir(path):
        image = path + "/poza_" + str(i) + ".png "
        text1 = '"And so the adventure begins." by me :p :))'
        time.sleep(a)
        with client(username, password) as cli:
            cli.upload(image, text1)
        i += 1


""" 
TODO: SEE TODO.txt !!!!!!

"""

if __name__ == '__main__':
    #RenameFiles()
    Upload()
