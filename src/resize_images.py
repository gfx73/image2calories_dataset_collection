from PIL import Image
import os
import concurrent.futures as cf
from constants import RESIZED_IMAGES_W, RESIZED_IMAGES_H, RESIZED_IMGS_DIR, DOWNLOADED_IMGS_DIR


def resize_image(image_filename: str):
    try:
        with Image.open(DOWNLOADED_IMGS_DIR / image_filename) as im:
            im = im.convert('RGB')
            resized = im.resize((RESIZED_IMAGES_W, RESIZED_IMAGES_H))
            resized.save(RESIZED_IMGS_DIR / image_filename)
    except Exception as e:
        print(image_filename)
        print(e)


def resize_images():
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(resize_image, os.listdir(DOWNLOADED_IMGS_DIR))


if __name__ == '__main__':
    resize_images()
