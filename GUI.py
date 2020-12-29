import eel
from main import search_image
eel.init("GUI")
search_image = eel.expose(search_image)

eel.start("home.html")
