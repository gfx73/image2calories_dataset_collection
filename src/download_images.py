import requests
import pandas as pd
import concurrent.futures as cf
from constants import REQUEST_IMAGES_W, REQUEST_IMAGES_H, DOWNLOAD_IMGS_ERRORS_PATH, DOWNLOAD_IMGS_LOGS_PATH,\
    DOWNLOADED_IMGS_DIR, FILTERED_FOODS_PATH
from utils import log_error, log_success, img_uri2filename


def download_img(uri: str, food_id: id):
    try:
        response = requests.get(
            'https://eda.yandex.ru/' + uri.format(REQUEST_IMAGES_W, REQUEST_IMAGES_H),
            headers={
                'scheme': 'https',
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru',
            }
        )
        response.raise_for_status()
    except requests.HTTPError as http_err:
        log_error(food_id, http_err, DOWNLOAD_IMGS_ERRORS_PATH, DOWNLOAD_IMGS_LOGS_PATH)
    except Exception as err:
        log_error(food_id, err, DOWNLOAD_IMGS_ERRORS_PATH, DOWNLOAD_IMGS_LOGS_PATH)
    else:
        img_filename = img_uri2filename(uri)
        with open(DOWNLOADED_IMGS_DIR / img_filename, 'wb') as f:
            f.write(response.content)
        log_success(food_id, DOWNLOAD_IMGS_LOGS_PATH)


def download_imgs():
    foods_df = pd.read_csv(FILTERED_FOODS_PATH)
    with cf.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_img, foods_df['picture_uri'], foods_df['id_'])


if __name__ == '__main__':
    download_imgs()
