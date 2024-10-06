import json
import os
from hyperlink import URL
import requests


def get_json_data(url: URL, output_dir) -> None:
    try:
        res = requests.get(url)
        print(res)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)

    json_data = res.json()
    output_file = url.split("/")[-1]
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
