import flask 

from main import app
from main.models import Entry, EnglishArchive
from main import db
from main.function import jp2en_transrator, get_file, get_record, URL, APPID, API_TOKEN
import requests
import glob
import random

@app.route('/')
def show_images():
    RESP = get_record(URL, API_TOKEN, APPID)

    data = []

    for item in RESP:
        ID = item["$id"]["value"]
        IMAGE = item["image"]["value"][0]["fileKey"]
        AREA = item["area"]["value"]
        get_file(URL, API_TOKEN, IMAGE, AREA, ID)
        # url = "https://api.ekispert.jp/v1/json/search/course/plain?key=eBBWPyXMYduCN759&from=35.70606813177083,139.651624325722,wgs84,2000&to=" + item["lat"]["value"] + ',' + item["lng"]["value"] + ",wgs84,2000"
        # response = requests.get(url)
        # jsonData = response.json()
        jsonData = {}
        one = {
            'id': item["$id"]["value"],
            'igame_id': item["image"]["value"][0]["fileKey"],
            'area': item["area"]["value"],
            'lat': item["lat"]["value"],
            'lng': item["lng"]["value"],
            'image': 'static/img/' + item["$id"]["value"] + '/' + item["area"]["value"] + '.png',
            'result': jsonData
        }
        data.append(one)
        random.shuffle(data)
    
    return flask.render_template('index.html', images_data = data)

@app.route('/test')
def show_images_test():
    RESP = get_record(URL, API_TOKEN, APPID)

    data = []

    for item in RESP:
        ID = item["$id"]["value"]
        IMAGE = item["image"]["value"][0]["fileKey"]
        AREA = item["area"]["value"]
        get_file(URL, API_TOKEN, IMAGE, AREA, ID)
        # url = "https://api.ekispert.jp/v1/json/search/course/plain?key=eBBWPyXMYduCN759&from=35.70606813177083,139.651624325722,wgs84,2000&to=" + item["lat"]["value"] + ',' + item["lng"]["value"] + ",wgs84,2000"
        # response = requests.get(url)
        # jsonData = response.json()
        jsonData = {}
        one = {
            'id': item["$id"]["value"],
            'igame_id': item["image"]["value"][0]["fileKey"],
            'area': item["area"]["value"],
            'lat': item["lat"]["value"],
            'lng': item["lng"]["value"],
            'image': 'static/img/' + item["$id"]["value"] + '/' + item["area"]["value"] + '.png',
            'result': jsonData
        }
        data.append(one)
        random.shuffle(data)
    
    return flask.render_template('test.html', images_data = data)