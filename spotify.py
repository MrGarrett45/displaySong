import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from the terminal
username = sys.argv[1]

# My ID: 12183287076

# Erase cache and prompt for user permission

token = util.prompt_for_user_token(username)

# Create spotify agent

spotify = spotipy.Spotify(auth=token)
