import eel, base64, collections
eel.init("GUI")

def search_image(name):
    file_list = sorted(glob.glob("{}/*{}.jpg".format(store_dir_name, name)))
    if file_list:
        return file_list
    return []

def img_to_b64(path):
    with open(path, "rb") as image:
        return base64.b64encode(image.read())

def format_image_to_dict(paths):
    images = collections.defaultdict(list)
    for path in paths:
        try:
            unix_time, date, name = path.split("-")
            name = name.rstrip(".jpg")
            images[name].append({"date":date, "img":img_to_b64(path).decode('utf-8')})
        except:
            print(f"ファイル\"{path}\"は撮影された画像ファイルではありません")
    return images


@eel.expose
def export_images(word):
    paths = search_image(word)
    if not paths:
        return None
    images = format_image_to_dict(paths)

    return images


# eel.get_recog_text()

eel.start("home/home.html", mode="custom", cmdline_args=['xdg-open', 'http://localhost:8000/home/home.html'])
