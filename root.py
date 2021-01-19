import eel
from bottle import Bottle, post, request, static_file

from main import store_dir_name

app = Bottle()
eel.init("GUI")

IMAGE_URL = "/images"
STATIC_URL = "/static"

STATIC_ROOT = "GUI"

del eel.BOTTLE_ROUTES["/<path:path>"]

for route_path, route_params in eel.BOTTLE_ROUTES.items():
    route_func, route_kwargs = route_params
    app.route(path=route_path, callback=route_func, **route_kwargs)


@app.route(IMAGE_URL + "<filename>")
def send_image(filename):
    return static_file(filename, root=store_dir_name, mimetype="image/jpeg")


@app.route(STATIC_URL + "<path:path>")
def send_static(path):
    return static_file(path, root=STATIC_ROOT)


@app.route("/home")
def home():
    return static_file("home/home.html", root=STATIC_ROOT)


@app.route("/log")
def log():
    return static_file("log/log.html", root=STATIC_ROOT)
