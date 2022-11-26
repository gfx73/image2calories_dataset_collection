import os

import pandas as pd
from constants import FILTERED_FOODS_PATH, DATASET_WITH_PATH, RESIZED_IMGS_DIR
from utils import img_uri2filename, img_filename2uri


def get_dataset_with_paths():
    filtered_foods_df = pd.read_csv(FILTERED_FOODS_PATH, index_col=0)

    resized_imgs_uris = [img_filename2uri(uri) for uri in os.listdir(RESIZED_IMGS_DIR)]
    filtered_foods_df = filtered_foods_df[filtered_foods_df['picture_uri'].isin(resized_imgs_uris)]
    filtered_foods_df['filename'] = filtered_foods_df['picture_uri'].apply(img_uri2filename)
    filtered_foods_df = filtered_foods_df.reset_index(drop=True)
    filtered_foods_df.to_csv(DATASET_WITH_PATH)


if __name__ == '__main__':
    get_dataset_with_paths()
