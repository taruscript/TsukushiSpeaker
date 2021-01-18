import base64
import collections

import eel
from bottle import Bottle, post, request

from main import search_image, store_dir_name


def img_to_b64(path):
    with open(path, "rb") as image:
        return base64.b64encode(image.read())


def format_image_to_dict(paths):
    images = collections.defaultdict(list)
    for path in paths:
        try:
            unix_time, date, name = path.split("-")
            name = name.rstrip(".jpg")
            images[name].append(
                {"date": date, "img": img_to_b64(path).decode("utf-8")})
        except:
            print(f'ファイル"{path}"は撮影された画像ファイルではありません')
    return images


app = Bottle()
eel.init("GUI")

for route_path, route_params in eel.BOTTLE_ROUTES.items():
    route_func, route_kwargs = route_params
    app.route(path=route_path, callback=route_func, **route_kwargs)


@app.route("/images/<filename:re:.*\.png>")
def send_image(filename):
    return static_file(filename, root="store_dir_name", mimetype="image/jpeg")


@eel.expose
def export_images(word):
    paths = search_image(word)
    if not paths:
        return None
    images = format_image_to_dict(paths)

    return images


eel.start(
    "home/home.html",
    mode="custom",
    cmdline_args=["xdg-open", "http://localhost:8000/home/home.html"],
    app=app,
)
