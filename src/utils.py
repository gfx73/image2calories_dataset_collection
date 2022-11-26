from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float


@dataclass(frozen=True)
class FoodInfo:
    id_: int
    name: str
    description: Optional[str]
    price: float
    picture_uri: Optional[str]
    public_id: Optional[str]
    weight_value: Optional[float]
    weight_unit: Optional[str]
    calories_value: Optional[float]
    calories_unit: Optional[str]
    carbohydrates_value: Optional[float]
    carbohydrates_unit: Optional[str]
    fats_value: Optional[float]
    fats_unit: Optional[str]
    proteins_value: Optional[float]
    proteins_unit: Optional[str]
    category_name: str


def log_error(index: int, error: Exception, errors_filepath: Path, logs_filepath: Path):
    with open(errors_filepath, 'a') as f:
        f.write(f'{error.__str__()} on index {index}\n')
    with open(logs_filepath, 'a') as f:
        f.write(f"error on index {index}\n")

    print(f'HTTP error occurred: {error}')


def log_success(index: int, logs_filepath: Path):
    with open(logs_filepath, 'a') as f:
        f.write(f"successfully downloaded {index}\n")
    print(f"successfully downloaded {index}")


def img_uri2filename(uri: str) -> str:
    return uri.replace('/', '_')


def img_filename2uri(filename: str) -> str:
    return filename.replace('_', '/')
