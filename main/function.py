
#!/usr/bin/python
# _*_ coding: utf-8 _*_

import requests
import json
import os

URL = "https://devgscrpd.cybozu.com/k/v1/"
APPID = 1
API_TOKEN = "cQLcDZmCe7NxOQQl3V74eEWsbcEhgWFJq543vi0V"

os.makedirs("main/static/img/", exist_ok=True)

def get_file(url, api_token, filekey, name, id):
    """kintoneのファイルをダウンロードする関数"""

    if os.path.exists("main/static/img/" + id):
      return
    else:
      headers = {"X-Cybozu-API-Token": api_token,'X-Requested-With': 'XMLHttpRequest'}
      resp = requests.get(url + "file.json" + '?fileKey=' + filekey, headers=headers)
      os.makedirs("main/static/img/" + id, exist_ok=False)
      f = open("main/static/img/" + id  + "/" + name + ".png", 'bw')
      f.write(resp.content)

def get_record(url, api_token, app):
    """kintoneのレコードを全件取得する関数"""
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(url + 'records.json' + '?app=' + str(app), headers=headers)

    return json.loads(resp.text)["records"]

def jp2en_transrator(string):
    result = requests.get('https://script.google.com/macros/s/AKfycbxjITyi5QlS-NhSAzg6BRQbiWPSK05qnOF1DYl9H_FC_4tzlOM/exec?text=' + string + '&source=ja&target=en')
    result.encoding

    return result.text