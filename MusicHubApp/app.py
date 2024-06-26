from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

# SoundCloud API base URL
SOUNDCLOUD_API_BASE_URL = "https://api.soundcloud.com"

# Spotify API credentials
CLIENT_ID = '8932344d682c47ce80a22d1f2d68ec21'
CLIENT_SECRET = '8c70649bb5a347209e5d1468c0df3f02'

# Spotify authorization endpoints
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

# Redirect URI for Spotify authorization flow
REDIRECT_URI = 'http://localhost:5000/callback'

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

@app.route('/artist_search')
def artist_search():
    return render_template('artist_search.html')

@app.route('/track_search')
def track_search():
    return render_template('track_search.html')

@app.route('/login')
def login():
    # Redirect the user to Spotify's authorization endpoint
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-private user-read-email',  # Add additional scopes as needed
    }
    auth_url = f'{AUTH_URL}?{"&".join([f"{key}={value}" for key, value in auth_params.items()])}'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Handle the callback from Spotify after user authorization
    code = request.args.get('code')
    if code:
        # Exchange the authorization code for an access token
        token_params = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
        response = requests.post(TOKEN_URL, data=token_params)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            # Use the access token to make requests to Spotify's API
            # Implement Spotify API functionality here
            return 'Authenticated successfully!'  # Placeholder response
    return 'Authorization failed!'

if __name__ == '__main__':
    app.run(debug=True)
