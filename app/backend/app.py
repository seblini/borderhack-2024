from flask import Flask
from urllib.request import urlopen
from dotenv import load_dotenv
import os
import sys

app = Flask(__name__)

@app.route("/")
def get_from_api():
    load_dotenv()
    API_KEY = os.getenv('MW_COLLEGIATE_API_KEY')
    print(API_KEY, file=sys.stderr)
    with urlopen(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/hello?key={API_KEY}') as r:
        text = r.read()
    return text