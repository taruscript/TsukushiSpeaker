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
                # wake word
                if "ＯＫ" in recog_text:
                    print("exec")
                    speech2Line()

                data = ""
            else:
                data += str(client.recv(1024).decode('utf-8'))
                print('NotFound')
    except KeyboardInterrupt:
        end_process(client)


if __name__ == "__main__":
    exist_check_julius()
    wait_for_OK()