# 個々のチャンピオン情報を取得する
import json
import os
from get_json_data import get_json_data
import itertools


def output_list_to_pyfile(data, file_name):
    list_data = list(data)
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"champ_ids = {repr(list_data)}\n")
    print(f"List successfully written to {file_path}")


def main():
    file_name = "champion.json"
    path = os.path.join(os.path.dirname(__file__), file_name)

    with open(path, "r", encoding="utf-8") as f:
        champ_dict = json.load(f)
    champ_ids = champ_dict["data"].keys()

    output_list_to_pyfile(champ_ids, "champ_ids.py")

    champ_dir_url = (
        "https://ddragon.leagueoflegends.com/cdn/14.19.1/data/ja_JP/champion"
    )

    urls = [f"{champ_dir_url}/{champ_id}.json" for champ_id in champ_ids]
    folder_name = "champ_indivisual"
    output_dir = os.path.join(os.path.dirname(__file__), folder_name)

    list(map(get_json_data, urls, itertools.repeat(output_dir)))


if __name__ == "__main__":
    main()
