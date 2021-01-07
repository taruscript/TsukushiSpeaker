import eel, base64
from main import search_image
eel.init("GUI")

def img_to_b64(path):
    with open(path, "rb") as image:
        return base64.b64encode(image.read())

@eel.expose
def export_image(word):
    paths = search_image(word)
    if not paths:
        return None
    images = {}
    for path in paths:
        unix_time, date, name = path.split("-")
        name = name.rstrip(".jpg")
        if not name in images:
            images[name] = {"date":date, "img":img_to_b64(path).decode('utf-8')}

    return images

# eel.start("home.html", mode="custom", cmdline_args=['xdg-open', 'http://localhost:8000/home.html'])
eel.start("home.html")
