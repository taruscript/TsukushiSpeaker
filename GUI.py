import eel, base64
from main import search_image
eel.init("GUI")

def img_to_b64(path):
    with open(path, "rb") as image:
        return base64.b64encode(image.read())

@eel.expose
def export_image(name):
    path = search_image(name)
    if path == "":
        return None
    image = img_to_b64(path).decode('utf-8')
    return image

eel.start("home.html", mode="custom", cmdline_args=['firefox', '-url', 'localhost:8000/home.html'])
