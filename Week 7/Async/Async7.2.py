import urllib.request 
import json

earthquake_url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"

response = urllib.request.urlopen(earthquake_url)
json_string = response.read().decode('utf-8')

eq_parsed_json = json.loads(json_string)
print(type(eq_parsed_json))
print((eq_parsed_json.keys())