from get_locations import get_all_cities
from download_layouts import download_layouts
from get_all_places import get_all_places
from deduplicate_places import deduplicate_places
from download_menus import download_menus
from get_foods import get_all_foods
from filter_foods import filter_foods
from download_images import download_imgs
from get_dataset_with_paths import get_dataset_with_paths
from resize_images import resize_images
import constants

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Collect the dataset')
    parser.add_argument('x_device_id', type=str, help='Your device id from eda.yandex.ru, check readme for details')
    parser.add_argument('-img_w', '--image_w', type=int, default=256, help='desired images width')
    parser.add_argument('-img_h', '--image_h', type=int, default=256, help='desired images height')
    args: argparse.Namespace = parser.parse_args()
    return args.x_device_id, args.image_w, args.image_h


def set_user_defined_consts(x_device_id: str, img_w: int, img_h: int):
    constants.X_DEVICE_ID = x_device_id
    constants.RESIZED_IMAGES_W = img_w
    constants.RESIZED_IMAGES_H = img_h


if __name__ == '__main__':
    set_user_defined_consts(*parse_args())
    get_all_cities()
    download_layouts()
    get_all_places()
    deduplicate_places()
    download_menus()
    get_all_foods()
    filter_foods()
    download_imgs()
    resize_images()
    get_dataset_with_paths()
