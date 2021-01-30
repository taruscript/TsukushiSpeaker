# -*- coding: utf-8 -*-
import requests
import subprocess
from subprocess import Popen
import socket
import voice
import psutil
import os
import time
import datetime
import shutil
from time import sleep
import conf
import pyaudio
import wave

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

def clean_images():
    try:
        shutil.rmtree("{}".format(conf.store_dir_name))
        os.makedirs(conf.store_dir_name, exist_ok=True)
        return True
    except:
        return False

def store_image(name):
    try:
        os.makedirs(conf.store_dir_name, exist_ok=True)
        file_name = "{}-{}-{}".format(time.time(), datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"), name)
        file_name = file_name.replace("[s]","").replace("[/s]","")
        cheese=['fswebcam','-F','3',"{}/{}.jpg".format(conf.store_dir_name, file_name)]
        subprocess.check_call(cheese)#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        return True
    except:
        return False

def notify_GUI(data):
    requests.post("http://localhost:8000/notify", data)


def music(wav_file):
    # チャンクサイズ(粒度)
    CHUNK_SIZE = 1024
 
    # WAVファイルを開く
    wf = wave.open(wav_file, 'rb')
 
    # PyAudioインスタンスを作成
    p = pyaudio.PyAudio()
 
    # Streamを開く。
    # フォーマットとはビット深度のことであり、
    # 8bitなら「p.get_format_from_width(1)」
    # 16bitなら「p.get_format_from_width((2)」とバイト数で設定
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
 
    # データをチャンクサイズだけ読み込む
    data = wf.readframes(CHUNK_SIZE)
 
    # Streamに読み取ったデータを書き込む＝再生する
    while len(data) > 0:
        # Streamに書き込む
        stream.write(data)
 
        # 再度チャンクサイズだけ読み込む。これを繰り返す
        data = wf.readframes(CHUNK_SIZE)
 
    # Streamを止めて、closeする。closeしなければ、start_stream()で再開
    stream.stop_stream()
    stream.close()
 
    # PyAudioインスタンスを破棄
    p.terminate()


def wait_for_OK():
    try:
        client = start_process()

        data = ""     # initialize data
        killword = '' # Variable to store the last recognize word
        while True:
            if '</RECOGOUT>\n.' in data:
                
                recog_text = ""
                #wakeword = "つくし"
                
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    
                    if index != -1:
                        line = line[index+6:line.find('"', index+6)]
                        recog_text = recog_text + line                      

                print("認識結果: " + recog_text)
                
                #murumur wake word
                if "つくし" in recog_text:
                    print("exec")
                    notify_GUI({"status": "started"})
                    killword = ("つくし" )
                   # sleep(1)
                    music("46.wav")
                    
                    print(killword)

                #murmur thing's name
                else:
                    if killword == ("つくし" ):
                        sleep(1)
                        music("49.wav")
                        print("picture")
                        store_image(recog_text)
                        killword = recog_text
                        notify_GUI({"status": "recognized", "text": recog_text})

                data = ""
            else:
                data += str(client.recv(1024).decode('utf-8'))
                print('NotFound')
    except KeyboardInterrupt:
       end_process(client) #Tsukushi end


if __name__ == "__main__":
    exist_check_julius()
    wait_for_OK()

