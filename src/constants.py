from pathlib import Path


REQUEST_IMAGES_W: int = 1920
REQUEST_IMAGES_H: int = 1080

RESIZED_IMAGES_W: int = 256
RESIZED_IMAGES_H: int = 256

X_DEVICE_ID: str = ''

CITIES_IN_COUNTRIES_DIR = Path('../required_datasets/cities_in_countries')
GENERATED_DATASETS_DIR = Path('../generated_datasets')
ERRORS_DIR = Path('../errors')
LOGS_DIR = Path('../logs')
LAYOUTS_DIR = Path('../retrieved_layouts')
MENUS_DIR = Path('../retrieved_menus')
DOWNLOADED_IMGS_DIR = Path('../downloaded_imgs')
RESIZED_IMGS_DIR = Path('../resized_imgs')

ALL_CITIES_PATH = GENERATED_DATASETS_DIR / 'all_cities.csv'
ALL_PLACES_PATH = GENERATED_DATASETS_DIR / 'all_places.csv'
DEDUPLICATED_PLACES_PATH = GENERATED_DATASETS_DIR / 'deduplicated_places.csv'
ALL_FOODS_PATH = GENERATED_DATASETS_DIR / 'all_foods.csv'
FILTERED_FOODS_PATH = GENERATED_DATASETS_DIR / 'filtered_foods.csv'
DATASET_WITH_PATH = GENERATED_DATASETS_DIR / 'dataset_with_paths.csv'


DOWNLOAD_LAYOUTS_ERRORS_PATH = ERRORS_DIR / 'download_layouts.txt'
DOWNLOAD_LAYOUTS_LOGS_PATH = LOGS_DIR / 'download_layouts.txt'
DOWNLOAD_MENUS_ERRORS_PATH = ERRORS_DIR / 'download_menus.txt'
DOWNLOAD_MENUS_LOGS_PATH = LOGS_DIR / 'download_menus.txt'
DOWNLOAD_IMGS_ERRORS_PATH = ERRORS_DIR / 'download_imgs.txt'
DOWNLOAD_IMGS_LOGS_PATH = LOGS_DIR / 'download_imgs.txt'

