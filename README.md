# Why TsukushiSpeaker?
このリポジトリはOKという言葉に反応し、Googleの音声認識のAPIが起動し、音声からテキストに変換する。次にそのテキストをLineNotifyに通知するというのが一連の流れ。


## setup
`pip3 install -r requirements.txt`

### ubuntu or debianの場合はこれも実行 (pipの実行のときにエラーが起きたらこれをインストすれば良いのかなlinuxは)
`sudo apt install python3-pyaudio`


### 下記のセットアップしたものをこのディレクトリに配置する。
https://qiita.com/fishkiller/items/dfd1b13a4380c6aa6322


# line tokenを作るときに便利なサイト
https://qiita.com/iitenkida7/items/576a8226ba6584864d95



# .envというファイルを作って、下記のような内容を書き込む


`TOKEN = LINE Notifyで作成したトークンをコピーしてペースト`