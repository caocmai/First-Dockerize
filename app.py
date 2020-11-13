import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def make_joke():
    params = { "limitTo": "nerdy"} # This sets params; needs to have correct key
    r = requests.get("http://api.icndb.com/jokes/random", params=params) # Using request to GET
    joke_json = r.json() # Need to call json to get or RECEIVE JSON data
    joke_str = joke_json["value"]["joke"] # Just takes the specific key pair
    return joke_str

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
