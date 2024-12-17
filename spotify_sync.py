import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

# Define your Spotify credentials
SPOTIFY_CLIENT_ID = 'd29a7dd1984d447b89933b50013b013e'
SPOTIFY_CLIENT_SECRET = '64bad87c8e824900a28188ea5e8644c6'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080/callback'  # Ensure this matches your Spotify app settings

# Set the scope for the authorization
SCOPE = 'playlist-modify-private playlist-modify-public'

# Authenticate and get the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=SCOPE))

def add_multiple_songs_to_playlist(songs, playlist_id):
    track_ids = []
    
    for song_name, artist_name in songs:
        query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=query, type='track', limit=1)
        
        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            track_ids.append(track_id)
            print(f"Found and added: '{song_name}' by {artist_name}")
        else:
            print(f"Song '{song_name}' by {artist_name} not found.")
    
    if track_ids:
        sp.playlist_add_items(playlist_id, track_ids)
        print("All found songs have been added to the playlist.")


files_to_playlists = [
    ["2020-2_new.csv", "1R1yQeTjIz08x8tDc2pzzi"],
    ["2021-1_new.csv", "4UkazJCsQSzNvngAM10YdK"],
    ["2021-2_new.csv", "4oOwcbZpKIgYRy9Z3l8Lid"],
    ["2022-1_new.csv", "0WANIk8Nsg7cS4yoyur8Kh"],
    ["2022-2_new.csv", "5drme0BVEVCamDRNNS3mc4"]
]


for file, playlist in files_to_playlists:
    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    songs_to_add = [(song[0], song[1]) for song in data]
    # add songs in groups of 98
    for i in range(0, len(songs_to_add), 98):
        add_multiple_songs_to_playlist(songs_to_add[i:i+98], playlist)
    # add_multiple_songs_to_playlist(songs_to_add, playlist)

# songs_to_add = [
#     ("Shape of You", "Ed Sheeran"),
#     ("Blinding Lights", "The Weeknd"),
#     ("Levitating", "Dua Lipa"),
#     ("Someone You Loved", "Lewis Capaldi")
# ]

# playlist_id = "4Cpl0AysvbOL8QN1GLGPhU"  # Replace with your playlist ID
# add_multiple_songs_to_playlist(songs_to_add, playlist_id)
