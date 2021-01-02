import eel
from main import search_image
eel.init("GUI")
search_image = eel.expose(search_image)

eel.start("home.html", mode="custom", cmdline_args=['firefox', '-url', 'localhost:8000/home.html'])
