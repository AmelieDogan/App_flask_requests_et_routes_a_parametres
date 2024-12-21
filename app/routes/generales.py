from ..app import app
from flask import render_template
import requests
import json

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id:str):

    url = 'https://www.wikidata.org/w/api.php'
    params = {
                'action': 'wbgetentities',
                'ids':id,
                'format': 'json',
                'languages': 'fr'
            }

    try:
        data = requests.get(url, params=params)
        code_http = data.status_code
        content_type = data.headers["Content-Type"]
        data = data.json()
    except:
        data = None

    if 'error' in data.keys() or data == None:
        data = None

    if data is not None:
        data = json.dumps(data, indent=2, ensure_ascii=False)

   
    return render_template("pages/wikidata_show.html", id=id, data=data, code_http=code_http, content_type=content_type)