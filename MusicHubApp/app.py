# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# SoundCloud API base URL
SOUNDCLOUD_API_BASE_URL = "https://api.soundcloud.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    artist_name = request.form['artist_name']

    # Make a request to SoundCloud API to search for tracks by artist
    response = requests.get(f"{SOUNDCLOUD_API_BASE_URL}/tracks", params={'q': artist_name})

    if response.status_code == 200:
        # Extract relevant information from the API response
        tracks = response.json()

        # Render template with search results
        return render_template('search_results.html', tracks=tracks)
    else:
        # Handle API error
        return "Error searching for tracks"

if __name__ == '__main__':
    app.run(debug=True)
