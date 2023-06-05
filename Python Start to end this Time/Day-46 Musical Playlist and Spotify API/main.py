
import requests
from bs4 import BeautifulSoup


CLIENT_ID = "b389a293f0d545e88926a91901d0a1ba"
CLIENT_SECRET = "30097b530b544cedb97e1fb53f67e5bb"


web_url = "https://gaana.com/playlist/sanjitdas12012to2015"
response = requests.get(web_url)
response_content = response.text
soup = BeautifulSoup(response_content, "html.parser")

year_input = input("Which year you want to travel ? Type the year.")


all_song_names = []
songs = soup.find_all(name="a", class_="_tra t_over _plyCr")
for song in songs:
    texts = song.getText().strip()
    all_song_names.append(texts)

new_line = "\n"

print(all_song_names)
with open("all_songs.txt", mode="w") as file:
    for each_song in range(len(all_song_names)):
        file.write(f"{each_song + 1}) {all_song_names[each_song]} {new_line}")








#
#
# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get("https://gaana.com/playlist/sanjitdas12012to2015" + date)
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
#
# #Spotify Authentication
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# print(user_id)
#
# #Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#
# #Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
#
#













