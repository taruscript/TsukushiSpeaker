import eel, base64, collections
import glob
import conf
eel.init("GUI")


def search_image(name):
    file_list = sorted(glob.glob("{}/*{}.jpg".format(conf.store_dir_name, name)))
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