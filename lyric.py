

# importing the requests library
import requests
import xml.etree.ElementTree as ET


# api-endpoint
URL = "http://api.chartlyrics.com/apiv1.asmx/SearchLyric"
print("please enter the artist name")
artist = input("artist: ")
print("please enter the song name")
song = input("song: ")


print()



# defining a params dict for the parameters to be sent to the API
PARAMS = {'artist': artist, 'song':song}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# here we are using xml element tree library to parse XML
# use .fromstring because we arent saving it to a file yet
tree = ET.fromstring(r.content)
root = ET.fromstring(r.content)

# these child tags are kind of weird. idk why
for child in root:
    print(child.tag, child.attrib)


print()
# this is the lyric checksum
print(root[0][1].text)
# This is the lyric ID for the top result of the search. With this ID we can make another requests and get the lyricsss
print(root[0][2].text)

lyricChecksum = root[0][1].text
lyricID = root[0][2].text
print("lyricChecksum: %s \nlyricID: %s" % (lyricChecksum, lyricID))

secondURL = "http://api.chartlyrics.com/apiv1.asmx/GetLyric"
secondParams = {'lyricID': lyricID, 'lyricCheckSum': lyricChecksum}

r2 = requests.get(url = secondURL, params= secondParams)
print()
print(r2.content)
lyricTree = ET.fromstring(r2.content)
lyricRoot = ET.fromstring(r2.content)
for child in lyricRoot:
    print(child.tag)

# here are our lyricsssss yahhhh

print(lyricRoot[9].text)



# future steps = save lyrics to a variable and split it up into a list/dic of words
# then count words
# find best algo for that operation



