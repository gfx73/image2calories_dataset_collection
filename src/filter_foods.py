from constants import ALL_FOODS_PATH, FILTERED_FOODS_PATH
import pandas as pd


def filter_foods():
    df = pd.read_csv(ALL_FOODS_PATH, index_col=0)

    df = df.dropna(subset=['picture_uri', 'weight_value', 'calories_value'])

    df = df.drop_duplicates(subset='public_id', ignore_index=True)
    df = df.drop_duplicates(subset='picture_uri', ignore_index=True)

    df['category_name'] = df['category_name'].str.lower()
    df = df[~df['category_name'].str.contains(r'напитки|чай|кофе|коктейли|смузи|соусы')]

    df['picture_uri'] = df['picture_uri'].str.replace(r'{w}|{h}', '{}')

    df = df.reset_index(drop=True)
    df.to_csv(FILTERED_FOODS_PATH)


if __name__ == '__main__':
    filter_foods()
