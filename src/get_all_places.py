import json
import os
import pandas as pd
from constants import LAYOUTS_DIR, ALL_CITIES_PATH, ALL_PLACES_PATH
from utils import Location


def get_places_of_layout(path: str, location: Location):
    with open(path, 'r') as f:
        json_data = json.load(f)

    if not json_data['data']:
        return [], [], [], []

    places_lists = json_data['data']['places_lists']

    # for one city(location)
    places_names: [str] = []
    places_slugs: [str] = []
    for places_list in places_lists:
        for place in places_list['payload']['places']:
            places_names.append(place['name'])
            places_slugs.append(place['slug'])

    places_latitude: [float] = [location.latitude] * len(places_names)
    places_longitude: [float] = [location.longitude] * len(places_names)
    return places_names, places_slugs, places_latitude, places_longitude


def get_all_places():
    all_cities = pd.read_csv(ALL_CITIES_PATH)

    all_places_names: [str] = []
    all_places_slugs: [str] = []
    all_places_latitude: [float] = []
    all_places_longitude: [float] = []

    layout_filename: str
    for layout_filename in os.listdir(LAYOUTS_DIR):
        city_id: int = int(layout_filename.split('.', 1)[0])
        places_names, places_slugs, places_latitude, places_longitude = \
            get_places_of_layout(LAYOUTS_DIR / layout_filename,
                                 Location(all_cities.iloc[city_id]['lat'], all_cities.iloc[city_id]['lng']))
        all_places_names += places_names
        all_places_slugs += places_slugs
        all_places_latitude += places_latitude
        all_places_longitude += places_longitude

    data = {'name': all_places_names,
            'slug': all_places_slugs,
            'latitude': all_places_latitude,
            'longitude': all_places_longitude}
    all_places_df = pd.DataFrame.from_dict(data)
    new_columns = all_places_df.columns.values
    new_columns[0] = 'id'
    all_places_df.columns = new_columns
    all_places_df.to_csv(ALL_PLACES_PATH)


if __name__ == '__main__':
    get_all_places()
