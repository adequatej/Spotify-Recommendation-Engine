### Spotify-Recommendation-Engine
This is a simple Spotify Recommendation Music Engine built using Python, Streamlit, and the Spotify API.

# About:
The Spotify Recommendation Engine allows users to input a song name and artist, along with their Spotify Client ID and Client Secret, and receive recommendations for similar songs.

# Installation
To use the Music Recommendation System, you'll need to follow these steps:

1. Install the required dependencies by running: "pip install streamlit spotipy"
2. Obtain a Spotify Client ID and Client Secret by registering your application on the Spotify Developer Dashboard.
3. Clone this repository
4. Navigte to your project directory 
5. Run using streamlit: "streamlit run spotify.py"

# Usage
Upon running the Streamlit app, you'll be prompted to enter a song name, artist, Spotify Client ID, and Spotify Client Secret.

Enter the required information and press "Enter".

The app will then display recommended songs based on the input song and artist.

# Algorithm

Spotify's track URI (Uniform Resource Identifier) system is a unique identifier that Spotify assigns to each piece of content on its platform, such as songs, albums, playlists, and artists. A URI in Spotify is used to reference and interact with a specific item in its vast library of content.

It allows to precisely search for or reference a specific song, album, or artist. By using this URI, you can retrieve detailed information about the track and use it for operations such as generating personalized music recommendations based on a seed track.

The Spotify API uses these URIs to handle requests and ensure that the correct content is being accessed or recommended.

# License
This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.
