# Why Speech2Line?
このリポジトリは音声を録音し、録音された音声データからGoogleの音声認識のAPIを使って、音声からテキストに変換する。次にそのテキストをLineNotifyに通知するというのが一連の流れ。


## setup
`pip3 install -r requirements.txt`

### ubuntu or debianの場合はこれも実行 (pipの実行のときにエラーが起きたらこれをインストすれば良いのかなlinuxは)
`sudo apt install python3-pyaudio`

# line tokenを作るときに便利なサイト
https://qiita.com/iitenkida7/items/576a8226ba6584864d95



# .envというファイルを作って、下記のような内容を書き込む


`TOKEN = LINE Notifyで作成したトークンをコピーしてペースト`