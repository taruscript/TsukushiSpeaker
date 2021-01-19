import collections
import os
import shutil

import eel

from main import search_image
from root import IMAGE_URL, app


def format_image_to_dict(paths):
    images = collections.defaultdict(list)
    for path in paths:
        try:
            path = os.path.basename(path)
            _, date, name = path.split("-")
            name = os.path.splitext(name)[0]
            images[name].append({"date": date, "img": IMAGE_URL + path})
        except:
            print(f'ファイル"{path}"は撮影された画像ファイルではありません')
    return images


@eel.expose
def export_images(word):
    paths = search_image(word)
    if not paths:
        return None
    images = format_image_to_dict(paths)

    return images


if shutil.which("xdg-open"):
    eel.start(
        "home/home.html",
        mode="custom",
        cmdline_args=["xdg-open", "http://localhost:8000/home"],
        app=app,
    )
else:
    eel.start(
        "home",
        app=app,
    )
