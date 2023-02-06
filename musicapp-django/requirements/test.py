# get api 

# Path: musicapp-django/requirements/local.py
# get api
import requests
# url = 'https://api.spotify.com/v1/search?q=artist:abba&type=album'
# # send the request with a token 
# token = "e7640cd0dfc54c27a4f8229a0f3c53de"
# response = requests.get(url, headers={'Authorization': 'Bearer ' + token})
# # response = requests.get(url)
# print(response.json())


#  spotify api tyo get las played songs
# https://developer.spotify.com/documentation/web-api/reference/player/get-recently-played/
# url = 'https://api.spotify.com/v1/me/player/recently-played'
# token = "e7640cd0dfc54c27a4f8229a0f3c53de"
# response = requests.get(url, headers={'Authorization': 'Bearer ' + token})
# print(response.json())


import requests

# Replace <ACCESS_TOKEN> with your actual Spotify Access Token
headers = {
    "Authorization": "Bearer e7640cd0dfc54c27a4f8229a0f3c53de"
}

# Get the User's recently played tracks
response = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers=headers)
print (response)
# Check if the "items" key exists in the response
if "items" in response.json():
    # Extract the last played track from the response
    last_played_track = response.json()["items"][0]["track"]

    # Print the track information
    print("Name:", last_played_track["name"])
    print("Artist:", last_played_track["artists"][0]["name"])
    print("Album:", last_played_track["album"]["name"])
else:
    # If the "items" key does not exist, print an error message
    print("Error: Unable to retrieve recently played tracks")