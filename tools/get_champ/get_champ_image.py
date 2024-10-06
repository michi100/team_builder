# チャンピオンの画像をスプラッシュアートを取得し、フォルダに格納する
import os
import json
import itertools
from champ_ids import champ_ids
from get_image import get_image
from const import CHAMP_IMAGE_OUTPUT_PATH


def main():
    dir_name = "champ_indivisual"
    skin_dict = {}
    for champ_id in champ_ids:
        file_name = f"{champ_id}.json"
        path = os.path.join(os.path.dirname(__file__), dir_name, file_name)
        with open(path, "r", encoding="utf-8") as f:
            champ_dict = json.load(f)
        skin_dict[champ_id] = [
            skin["num"] for skin in champ_dict["data"][champ_id]["skins"]
        ]

    splash_dir_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash"
    urls = []

    for champ_id, skin_numbers in skin_dict.items():
        for skin_number in skin_numbers:
            urls.append(f"{splash_dir_url}/{champ_id}_{skin_number}.jpg")

    list(map(get_image, urls, itertools.repeat(CHAMP_IMAGE_OUTPUT_PATH)))


if __name__ == "__main__":
    main()
