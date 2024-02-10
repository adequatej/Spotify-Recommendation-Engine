import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Function to get Spotify recommendations 
def get_recommendations(track_name, artist, client_id, client_secret):
    
    # Validate client ID and client secret
    if not client_id or not client_secret:
        st.error("Please provide your Spotify Client ID and Client Secret.")
        return None

    # Set up Spotify credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Get track URI
    results = sp.search(q=f"track:{track_name} artist:{artist}", type='track')
    if not results['tracks']['items']:
        return None
    track_uri = results['tracks']['items'][0]['uri']

    # Get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

# Main app
def main():
    # Streamlit app title
    st.title("Music Recommendation System")

    # For users to enter the name of the track and artist they want recommendations for
    track_name = st.text_input("Enter a song name:")
    artist = st.text_input("Enter the artist:")
    
    # Get Spotify credentials from user input
    client_id = st.text_input("Enter your Spotify Client ID:")
    client_secret = st.text_input("Enter your Spotify Client Secret:", type="password")

    # To check if the user has entered track name, artist, client ID, and client secret
    if track_name and artist and client_id and client_secret:
        recommendations = get_recommendations(track_name, artist, client_id, client_secret)
        if recommendations:
            st.write("Recommended songs:")
            for track in recommendations:
                st.write(track['name'])
                st.image(track['album']['images'][0]['url'])
        else:
            st.write("No recommendations found for the given track name and artist.")

if __name__ == "__main__":
    main()
=======
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Function to get Spotify recommendations 
def get_recommendations(track_name, artist, client_id, client_secret):
    # Validate client ID and client secret
    if not client_id or not client_secret:
        st.error("Please provide your Spotify Client ID and Client Secret.")
        return None

    # Set up Spotify credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Get track URI
    results = sp.search(q=f"track:{track_name} artist:{artist}", type='track')
    if not results['tracks']['items']:
        return None
    track_uri = results['tracks']['items'][0]['uri']

    # Get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

# Main app
def main():
    # Streamlit app title
    st.title("Music Recommendation System")

    # For users to enter the name of the track and artist they want recommendations for
    track_name = st.text_input("Enter a song name:")
    artist = st.text_input("Enter the artist:")
    
    # Get Spotify credentials from user input
    client_id = st.text_input("Enter your Spotify Client ID:")
    client_secret = st.text_input("Enter your Spotify Client Secret:", type="password")

    # To check if the user has entered track name, artist, client ID, and client secret
    if track_name and artist and client_id and client_secret:
        recommendations = get_recommendations(track_name, artist, client_id, client_secret)
        if recommendations:
            st.write("Recommended songs:")
            for track in recommendations:
                st.write(track['name'])
                st.image(track['album']['images'][0]['url'])
        else:
            st.write("No recommendations found for the given track name and artist.")

if __name__ == "__main__":
    main()
