from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import request

import requests

@app.route('/artist_search')
def artist_search():
    artist_name = request.args.get('artist_name')
    # Make a GET request to the Spotify API
    response = requests.get('https://api.spotify.com/v1/search', params={'q': artist_name, 'type': 'artist'})
    # Parse the JSON response and extract the list of artists
    artists = response.json()['artists']['items']
    # Now you have the list of artists, proceed with rendering the search results template.


@app.route('/artist/<artist_id>')
def artist(artist_id):
    # Placeholder for fetching artist information
    # Replace this with your implementation to fetch data from Spotify API
    artist_info = {
        'id': artist_id,
        'name': 'Artist Name',
        'genre': 'Genre',
        'popularity': 'Popularity'
    }
    return render_template('artist.html', artist=artist_info)

@app.route('/track/<track_id>')
def track(track_id):
    # Placeholder for fetching track information
    # Replace this with your implementation to fetch data from Spotify API
    track_info = {
        'id': track_id,
        'name': 'Track Name',
        'artist': 'Artist Name',
        'album': 'Album Name',
        'release_date': 'Release Date'
    }
    return render_template('track.html', track=track_info)

@app.route('/artist_search')
def artist_search():
    # Add your implementation here
    pass

if __name__ == '__main__':
    app.run(debug=True)
