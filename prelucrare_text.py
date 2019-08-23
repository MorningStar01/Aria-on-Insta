import os
import sys


def ModText():
    with open('text1.txt', 'r+') as text:
        for line in text.readlines():
            # print(line, end='')
            start = line.find("<blockquote><p>")
            end = line.find("</p></blockquote>", start)
            curat = line[start + 15:end]
            #print("->" + curat)
            s = curat[0:28]
            #print(repr(s))
    text = open("text3.txt", "w")

    print("->" + s, end="")


if __name__ == '__main__':
    ModText()