from constants import ALL_PLACES_PATH, DEDUPLICATED_PLACES_PATH
import pandas as pd


def deduplicate_places():
    all_places_df = pd.read_csv(ALL_PLACES_PATH, index_col=0)
    deduplicate_places_df = all_places_df.drop_duplicates(subset='slug', ignore_index=True)
    deduplicate_places_df.to_csv(DEDUPLICATED_PLACES_PATH)


if __name__ == '__main__':
    deduplicate_places()
