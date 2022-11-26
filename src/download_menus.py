import requests
import json
import pandas as pd
from typing import Iterable
import concurrent.futures as cf
from utils import Location, log_success, log_error
from constants import DOWNLOAD_MENUS_LOGS_PATH, DOWNLOAD_MENUS_ERRORS_PATH, MENUS_DIR, DEDUPLICATED_PLACES_PATH


def download_menu(location: Location, place_slug: str, place_id: int):
    try:
        response = requests.get(
            f'https://eda.yandex.ru/api/v2/menu/retrieve/{place_slug}?longitude={location.longitude}&latitude={location.latitude}&autoTranslate=false',
            headers={
                'scheme': 'https',
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru',
            }
        )
        response.raise_for_status()
    except requests.HTTPError as http_err:
        log_error(place_id, http_err, DOWNLOAD_MENUS_ERRORS_PATH, DOWNLOAD_MENUS_LOGS_PATH)
    except Exception as err:
        log_error(place_id, err, DOWNLOAD_MENUS_ERRORS_PATH, DOWNLOAD_MENUS_LOGS_PATH)
    else:
        json_response = response.json()
        with open(MENUS_DIR / f'{place_id}.json', 'w') as f:
            json.dump(json_response, f)
        log_success(place_id, DOWNLOAD_MENUS_LOGS_PATH)


def download_menus():
    deduplicated_places_df = pd.read_csv(DEDUPLICATED_PLACES_PATH)
    locations: Iterable[Location] = map(lambda lat_and_long: Location(*lat_and_long),
                                        zip(deduplicated_places_df['latitude'], deduplicated_places_df['longitude']))
    slugs: [str] = deduplicated_places_df['slug'].tolist()
    ids: [id] = deduplicated_places_df.index.tolist()
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_menu, locations, slugs, ids)


if __name__ == '__main__':
    download_menus()
