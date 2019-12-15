import requests
import json

url = "https://api.ekispert.jp/v1/json/search/course/plain?key=eBBWPyXMYduCN759&from=35.70606813177083,139.651624325722,wgs84,2000&to=35.68042009453629,139.7690262983716,wgs84,2000"
response = requests.get(url)
jsonData = response.json()
print(type(jsonData))
print(jsonData)