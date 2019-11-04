## python file to handle requests to the earthquake API
import requests, json

def get_lastDay(save):
    request_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson'
    response = requests.get(request_url)
    earthquakes_data = []
    if response.status_code == 200:
        response_json = json.loads(response.text)
        for feature in response_json['features']:
            if feature['type'] == 'Feature':
                feature_data = get_dict(feature['properties'])
                feature_data['location'] = get_location(feature['geometry'])
                print(feature_data)
                earthquakes_data.append(feature_data)
    if save == 'json':
        save_json(earthquakes_data)
    elif save == 'db':
        print('TODO save to DB')
    return 0

def get_dict(dataset):
    earthquake_data = {}
    earthquake_data['time'] = dataset['time']
    earthquake_data['place'] = dataset['place']
    earthquake_data['mag'] = dataset['mag']
    earthquake_data['significant'] = dataset['sig']
    if dataset['tsunami'] == 1:
        earthquake_data['tsunami_warning'] = True
    else:
        earthquake_data['tsunami_warning'] = False
    earthquake_data['type'] = dataset['type']
    return earthquake_data


def get_location(loc):
    location = []
    if loc['type'] == 'Point':
        location.append(loc['coordinates'][1])
        location.append(loc['coordinates'][0])
    return location


def save_json(data):
    if len(data) > 0:
        with open('earthquakes.json', 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    return 0

