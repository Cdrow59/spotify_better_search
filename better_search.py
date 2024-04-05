import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

def search_spotify_tracks(search_query):
    # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify API credentials
    client_id = '3b034fdee1384ddf9d0808cbc7fd948f'
    client_secret = '2ec30698b3484ca9bd2a7e7ae640e3eb'
    redirect_uri = 'http://localhost:8000/callback'

    filename = (os.path.splitext(os.path.basename(__file__))[0])
    cache_path = ("C:\\Users\\Clayton\\AppData\\Local\\Temp\\vscode\\" +filename+ ".cache")
    
    # Initialize Spotipy with client credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,cache_path=cache_path))

# Get user input for return query
    return_query = input("Enter your return query: ")

    # Get user input for the number of results to return
    num_results = int(input("Enter the number of results to return: "))

    # Get user input for sorting order
    sorting_order = input("Enter sorting order (e.g., 'popularity', 'name', 'release_date'): ")

    # Search for tracks with specified query
    results = results = sp.search(q=search_query, type='track', limit=num_results, market='US', offset=0)

    # Sort the results based on the chosen sorting order
    if sorting_order == 'popularity':
        results['tracks']['items'].sort(key=lambda x: x['popularity'], reverse=True)
    elif sorting_order == 'name':
        results['tracks']['items'].sort(key=lambda x: x['name'])
    elif sorting_order == 'release_date':
        results['tracks']['items'].sort(key=lambda x: x['album']['release_date'])
# Add other sorting conditions as needed
    # Display information about each matching track
    for index, track_info in enumerate(results.get('tracks', {}).get('items', []), 1):
        track_id = track_info['id']

        try:
            # Get track information
            track_info = sp.track(track_id)
            audio_features = sp.audio_features([track_id])[0]

            # Get the first artist's information to infer the genre
            artist_info = sp.artist(track_info['artists'][0]['id'])

            # Display track information
            # Display track information
            print(f"\nSearch Result #{index}")
            if 'name' or '*' in return_query:
                if '-name' not in return_query:
                    print(f"Track: {track_info['name']}")
            if 'artist' or '*' in return_query:
                print(f"Artist: {', '.join([artist['name'] for artist in track_info['artists']])}")
            if 'album' or '*' in return_query:
                print(f"Album: {track_info['album']['name']}")
            if 'release_date' or '*' in return_query:
                print(f"Release Date: {track_info['album']['release_date']}")
            if 'duration' or '*' in return_query:
                print(f"Duration: {audio_features['duration_ms'] / 1000} seconds")
            if 'tempo' or '*' in return_query:
                print(f"Tempo (BPM): {audio_features['tempo']}")
            if 'key' or '*' in return_query:
                print(f"Key: {audio_features['key']}")
                print(f"Camelot: {audio_features['key'] % 12}A")
            if 'popularity' or '*' in return_query:
                print(f"Popularity: {track_info['popularity']}")
            if 'happiness' or '*' in return_query:
                print(f"Happiness: {audio_features['valence']}")
            if 'danceability' or '*' in return_query:
                print(f"Danceability: {audio_features['danceability']}")
            if 'energy' or '*' in return_query:
                print(f"Energy: {audio_features['energy']}")
            if 'acousticness' or '*' in return_query:
                print(f"Acousticness: {audio_features['acousticness']}")
            if 'instrumentalness' or '*' in return_query:
                print(f"Instrumentalness: {audio_features['instrumentalness']}")
            if 'liveness' or '*' in return_query:
                print(f"Liveness: {audio_features['liveness']}")
            if 'speechiness' or '*' in return_query:
                print(f"Speechiness: {audio_features['speechiness']}")
            if 'loudness' or '*' in return_query:
                print(f"Loudness: {audio_features['loudness']} dB")
            if 'explicit' or '*' in return_query:
                print(f"Explicit: {track_info['explicit']}")
        except KeyError as e:
            print(f"Error: {e}")
            print("Some required keys are missing in the Spotify API response.")

if __name__ == "__main__":
    # Get user input for the search query
    user_search_query = input("Enter your search query: ")
    
    # Call the function with the search query
    search_spotify_tracks(user_search_query)