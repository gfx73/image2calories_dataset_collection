import json
from typing import Optional, Tuple
import pandas as pd
import os
from pathlib import Path
from constants import MENUS_DIR, ALL_FOODS_PATH
from utils import FoodInfo


def get_food_info(food, category_name) -> FoodInfo:
    def get_nutrient_data(nutrients_, name_) -> Tuple[Optional[float], Optional[str]]:
        if name_ in nutrients_:
            data = nutrients_[name_]
            value: Optional[float] = data['value'] if 'value' in data else None
            unit: Optional[str] = data['unit'] if 'unit' in data else None
            return value, unit
        else:
            return None, None

    id_: int = food['id']
    name: str = food['name']
    description: Optional[str] = food['description'] if 'description' in food else None
    price: float = food['price']
    picture_uri: Optional[str] = food['picture']['uri'] if 'picture' in food else None
    public_id: Optional[str] = food['publicId'] if 'publicId' in food else None
    weight_value: Optional[float] = food['measure']['value'] if 'measure' in food else None
    weight_unit: Optional[str] = food['measure']['measure_unit'] if 'measure' in food else None
    calories_value: Optional[float] = None
    calories_unit: Optional[str] = None
    carbohydrates_value: Optional[float] = None
    carbohydrates_unit: Optional[str] = None
    fats_value: Optional[float] = None
    fats_unit: Optional[str] = None
    proteins_value: Optional[float] = None
    proteins_unit: Optional[str] = None

    if 'nutrients' in food:
        nutrients = food['nutrients']
        calories_value, calories_unit = get_nutrient_data(nutrients, 'calories')
        carbohydrates_value, carbohydrates_unit = get_nutrient_data(nutrients, 'carbohydrates')
        fats_value, fats_unit = get_nutrient_data(nutrients, 'fats')
        proteins_value, proteins_unit = get_nutrient_data(nutrients, 'proteins')

    food_info = FoodInfo(
        id_,
        name,
        description,
        price,
        picture_uri,
        public_id,
        weight_value,
        weight_unit,
        calories_value,
        calories_unit,
        carbohydrates_value,
        carbohydrates_unit,
        fats_value,
        fats_unit,
        proteins_value,
        proteins_unit,
        category_name)

    return food_info


def get_foods_info_in_menu(menu_path: Path) -> [FoodInfo]:
    with open(menu_path, 'r') as f:
        json_data = json.load(f)

    food_infos: [FoodInfo] = []
    for category in json_data['payload']['categories']:
        if 'id' not in category:
            continue
        category_name = category['name']
        for food in category['items']:
            food_info = get_food_info(food, category_name)
            food_infos.append(food_info)
    return food_infos


def get_all_foods():
    food_infos: [FoodInfo] = []
    menu_path: str
    for menu_path in os.listdir(MENUS_DIR):
        try:
            food_infos_in_menu = get_foods_info_in_menu(MENUS_DIR / menu_path)
        except KeyError:
            print(menu_path)
            raise KeyError
        food_infos += food_infos_in_menu

    all_foods_df = pd.DataFrame(food_infos)
    all_foods_df.to_csv(ALL_FOODS_PATH)


if __name__ == '__main__':
    get_all_foods()
