#!/usr/bin/python3
import requests
import xml.etree.ElementTree as ET

URL = "http://api.chartlyrics.com/apiv1.asmx/SearchLyric"
artist = input("please enter the artist name: ")
song = input("please enter the song name: ")
PARAMS = {'artist': artist, 'song':song}

def getLyrics():
    r = requests.get(url=URL, params=PARAMS)
    if (len(r.content) > 385):
        tree = ET.fromstring(r.content)
        root = ET.fromstring(r.content)

        lyricChecksum = root[0][1].text
        lyricID = root[0][2].text

        secondURL = "http://api.chartlyrics.com/apiv1.asmx/GetLyric"
        secondParams = {'lyricID': lyricID, 'lyricCheckSum': lyricChecksum}

        r2 = requests.get(url=secondURL, params=secondParams)
        print()

        lyricTree = ET.fromstring(r2.content)
        lyricRoot = ET.fromstring(r2.content)

        if (lyricRoot[4].text.lower() == artist.lower()):
            print("This lyric is available!\n\n")
            print(lyricRoot[9].text)
        else:
            print("This lyric is unavailable. Check your spelling please.")
    else:
        print("Try again please")
    lyricString = lyricRoot[9].text
    return lyricString

def countWords(lyric):
    lyricStripped = lyric.strip()

    counter = 0
    for line in lyricStripped.splitlines(True):
        for char in line:
            if(char == " "):
                counter += 1
            elif(char == "\n" and len(line) > 1):
                counter += 1
            else:
                counter = counter
    print("Number of words: %d" % counter)

    # according to wordcounter.net and wordcounter.io we are off by 1 word lol
    # we can just add 1 to it but uhhhh lol

def mostUsedWords():
    # make most used algo
    mostUsedDict = {}
    return mostUsedDict


lyricString = getLyrics()
countWords(lyricString)


