from services import earthquake
from tools import time
import json
from operator import itemgetter

def get_data(type):
    ## Get data from all required services and combine in one json. For now just run
    if 'earthquake' in type:
        earthquake.get_lastDay('json')
    disaster_json = combine_for_export(type)
    with open('disasters.json', 'w', encoding="utf-8") as file:
        json.dump(disaster_json, file, ensure_ascii=False, indent=4)
    return 0

def combine_for_export(type):
    combined = []
    for item in type:
        if item == 'earthquake':
            with open('earthquakes.json', encoding="utf-8") as earthquake_file:
                earthquakes = json.load(earthquake_file)
                for element in earthquakes:
                    temp_data = {}
                    temp_data['date'] = element['time']
                    temp_data['type'] = element['type']
                    temp_data['location'] = element['place']
                    additional_string = 'Magnitude: ' + str(round(element['mag'],1)) + ", Significant level: " + str(element['significant'])
                    temp_data['additional_info'] = additional_string
                    combined.append(temp_data)
    combined = sorted(combined, key=itemgetter('date'), reverse=True)
    for element in combined:
        element['date'] = time.timefrommiliseconds(element['date'])
    return combined