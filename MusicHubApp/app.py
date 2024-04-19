from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artist_search')
def artist_search():
    # Get the search query from the request parameters
    query = request.args.get('query')
    
    # Make a request to the Spotify API to search for artists
    # Replace 'YOUR_ACCESS_TOKEN' with your actual access token
    headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    params = {'q': query, 'type': 'artist'}
    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the artist data from the response
        data = response.json()
        artists = data.get('artists', {}).get('items', [])
        
        # Return the list of artists as JSON response
        return jsonify({'artists': artists})
    else:
        # If the request was not successful, return an error message
        return jsonify({'error': 'Failed to search for artists'})

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

if __name__ == '__main__':
    app.run(debug=True)
