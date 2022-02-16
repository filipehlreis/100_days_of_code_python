import os
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"

print()
input_date = input(
    "Qual ano voce deseja buscar?\n"
    "Digite a data no seguinte formato YYYY-MM-DD: "
)

url_search = f"https://www.billboard.com/charts/hot-100/{input_date}"

response = requests.get(url=url_search)
response.raise_for_status()

data = response.text

soup = BeautifulSoup(data, "html.parser")

all_songs_tag = soup.select("li ul li h3")
all_songs = [song.getText().strip() for song in all_songs_tag]

spotify_app = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="day46\\token.txt",
        show_dialog=True
    )
)

user_id = spotify_app.current_user()["id"]
songs_uri = []
year_music = input_date.split('-')[0]

for name_music in all_songs:
    query = f"track:{name_music} year:{year_music}"

    try:
        result = spotify_app.search(q=query, type="track")
        track_uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(track_uri)
        pprint(track_uri)
    except IndexError:
        print(f"A musica '{name_music}' nao existe no Spotify.")

playlist = spotify_app.user_playlist_create(
    user=user_id,
    name=f"{input_date} Billboard 100",
    public=False
)

spotify_app.playlist_add_items(
    playlist_id=playlist["id"],
    items=songs_uri
)
