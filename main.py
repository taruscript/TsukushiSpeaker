# -*- coding: utf-8 -*-
import subprocess
import socket
import line_notice
import voice
from time import sleep
import psutil


host = "localhost"
port = 10500


#　juliusのプロセスが存在するかチェック。
def exist_check_julius():
    process_name = "julius"

    for proc in psutil.process_iter():
        # プロセスチェックをしてあったらkillをする
        if proc.name() == process_name:
            proc.terminate()


def start_process():    
    subprocess.Popen(["./julius-start.sh"], stdout=subprocess.PIPE, shell=True)
    # Juliusにソケット通信で接続
    sleep(3)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client


def end_process(client):
    print('finished')
    client.send("DIE".encode('utf-8'))
    client.close()

def speech2Line():
    voice_class = voice.voiceFunctionsClass()
    voice_class.voice_recode()
    voice_result = voice_class.voice_recognize()
    line_notice.send(voice_result)

def get_picture():
    cheese=['fswebcam','-D','1','image.jpg']
    try:
        subprocess.check_call(cheese)
        print ("Command finished.")
    except:
        return "Command envailed."

def store_image(name):
    filename = "{}-{}-{}.jpg".format(time.time(), datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"), name)
    shutil.copyfile("image.jpg", "./images/{}".format(filename))
    #print(filename)

def search_image(name):
    filelist = sorted(glob.glob("./images/*{}.jpg".format(name)))
    X = 255
    Y = 255
    print(filelist[-1])
    root = tk.Tk()
    root.title("TsukushiSpeaker")
    root.minsize(X, Y)
    image = tk.PhotoImage(file=filelist[-1])
    canvas = tk.Canvas(bg="white", width=X, height=Y)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=image, anchor=tk.NW)
    root.mainloop()

def delete_images():
    shutil.rmtree("./images/")
    os.mkdir("./images/")

def wait_for_OK():
    try:
        client = start_process()

        data = ""
        while True:
            if '</RECOGOUT>\n.' in data:


                recog_text = ""
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index+6:line.find('"', index+6)]
                        recog_text = recog_text + line
                print("認識結果: " + recog_text)
                store_image(recog_text)
                #search_image("検索するファイル名")
                #delete_images()
                # wake word
                if "ＯＫ" in recog_text:
                    print("exec")
                    speech2Line()
                    get_picture()

                data = ""
            else:
                data += str(client.recv(1024).decode('utf-8'))
                print('NotFound')
    except KeyboardInterrupt:
        end_process(client)


if __name__ == "__main__":
    exist_check_julius()
    wait_for_OK()