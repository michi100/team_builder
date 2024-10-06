import requests
import os


def get_image(url, output_dir) -> None:
    try:
        res = requests.get(url)
        print(res)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)

    image = res.content
    file_name = url.split("/")[-1]
    path = os.path.join(output_dir, file_name)
    with open(path, "wb") as f:
        f.write(image)
