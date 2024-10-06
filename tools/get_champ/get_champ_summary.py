# チャンピオンサマリ情報を取得する
import os
from tools.get_champ import get_json_data


def main():
    url = "https://ddragon.leagueoflegends.com/cdn/14.19.1/data/ja_JP/champion.json"
    output_dir = os.path.dirname(__file__)

    get_json_data(url, output_dir)


if __name__ == "__main__":
    main()
