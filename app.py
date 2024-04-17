from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

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
