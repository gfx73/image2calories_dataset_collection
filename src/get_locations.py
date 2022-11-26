import pandas as pd
import os
from constants import CITIES_IN_COUNTRIES_DIR, ALL_CITIES_PATH


def get_all_cities():
    dataframes = []
    for df_filename in os.listdir(CITIES_IN_COUNTRIES_DIR):
        dataframes.append(pd.read_csv(CITIES_IN_COUNTRIES_DIR / df_filename))

    all_cities = pd.concat(dataframes)
    all_cities = all_cities.reset_index(drop=True)
    all_cities.to_csv(ALL_CITIES_PATH)


if __name__ == '__main__':
    get_all_cities()
