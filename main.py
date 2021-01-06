# -*- coding: utf-8 -*-
import subprocess
from subprocess import Popen
import socket
import line_notice
import voice
import psutil
import os
import time
import datetime
import shutil
import glob
from time import sleep

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

store_dir_name = "images"

def store_image(name):
    try:
        os.makedirs(store_dir_name, exist_ok=True)
        file_name = "{}-{}-{}".format(time.time(), datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"), name)
        file_name = file_name.replace("[s]","").replace("[/s]","")
        cheese=['fswebcam','-F','80',"{}/{}.jpg".format(store_dir_name, file_name)]
        subprocess.check_call(cheese)#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        return True
    except:
        return False

def search_image(name):
    file_list = sorted(glob.glob("{}/*{}.jpg".format(store_dir_name, name)))
    if file_list:
        return file_list[-1]
     
    return ""

def clean_images():
    try:
        shutil.rmtree("{}".format(store_dir_name))
        os.makedirs(store_dir_name, exist_ok=True)
        return True
    except:
        return False

def wait_for_OK():
    try:
        client = start_process()

        data = ""     # initialize data
        killword = '' # Variable to store the last recognize word
        while True:
            if '</RECOGOUT>\n.' in data:
                
                recog_text = ""
                
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    
                    if index != -1:
                        line = line[index+6:line.find('"', index+6)]
                        recog_text = recog_text + line                      

                print("認識結果: " + recog_text)
                
                #murumur wake word
                if "らずぱい" in recog_text:
                    print("exec")
                    killword = ("らずぱい" )            
                    print(killword)

                #elif "だいどころ" in recog_text:
                 #   print("search")
                  #  killword = ("だいどころ" )            
                   # print(killword)

                #murmur thing's name
                else:
                    if killword == ("らずぱい" ):
                        sleep(1)
                        print("picture")
                        store_image(recog_text)
                        killword = recog_text

                    #elif killword == ("だいどころ"):
                     #   sleep(1)
                      #  print("search picture")

                       # killword = recog_text
        
                data = ""
            else:
                data += str(client.recv(1024).decode('utf-8'))
                print('NotFound')
    except KeyboardInterrupt:
       end_process(client) #Tsukushi end


if __name__ == "__main__":
    exist_check_julius()
    wait_for_OK()
