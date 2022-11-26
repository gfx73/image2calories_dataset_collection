import requests
import json
import pandas as pd
from constants import X_DEVICE_ID, LAYOUTS_DIR, ALL_CITIES_PATH, DOWNLOAD_LAYOUTS_ERRORS_PATH,\
    DOWNLOAD_LAYOUTS_LOGS_PATH
from utils import Location, log_error, log_success


def download_layout_for_city(location: Location, city_index: int):
    location_data = json.dumps({
        "location": {
            "latitude": location.latitude,
            "longitude": location.longitude
        },
        "filters": []
    })
    try:
        response = requests.post('https://eda.yandex.ru/eats/v1/layout-constructor/v1/layout',
                                 data=location_data,
                                 headers={'authority': 'eda.yandex.ru',
                                          'method': 'POST',
                                          'path': '/eats/v1/layout-constructor/v1/layout',
                                          'scheme': 'https',
                                          'accept': 'application/json',
                                          'accept-encoding': 'gzip, deflate, br',
                                          'content-type': 'application/json;charset=UTF-8',
                                          'x-device-id': X_DEVICE_ID,
                                          }
                                 )
        response.raise_for_status()
    except requests.HTTPError as http_err:
        log_error(city_index, http_err, DOWNLOAD_LAYOUTS_ERRORS_PATH, DOWNLOAD_LAYOUTS_LOGS_PATH)
    except Exception as err:
        log_error(city_index, err, DOWNLOAD_LAYOUTS_ERRORS_PATH, DOWNLOAD_LAYOUTS_LOGS_PATH)
    else:
        json_response = response.json()
        with open(f'{LAYOUTS_DIR}{city_index}.json', 'w') as f:
            json.dump(json_response, f)
        log_success(city_index, DOWNLOAD_LAYOUTS_LOGS_PATH)


def download_layouts():
    all_cities = pd.read_csv(ALL_CITIES_PATH)
    city_index: int
    for city_index, row in all_cities.iterrows():
        download_layout_for_city(Location(row['lat'], row['lng']), city_index)


if __name__ == '__main__':
    download_layouts()
