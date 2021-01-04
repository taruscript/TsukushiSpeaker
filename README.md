
# TsukushiSpeaker
家の中でのなくしものをなくすための便利な道具、TsukushiSpeaker。

<!--
初期段階からSNS宣伝とかして、変更過程も発表する予定です。
作りたい最終形態と現在の状況を掲載します。
-->

### 目次
1. TsukushiSpeakerとは
2. 仕組み
3. 準備する物
4. インストール方法
・Ubuntu
・Raspberry Pi(これから対応予定)
5. トラブルシューティング
6. 連絡先

## 1. TsukushiSpeakerとは
<!-- 
全体像としてはこんな感じで作りたいんです。
理由としてはこうゆう感じです。
-->

外出する時に「あれ！家の鍵がない！」と慌てた事はありませんか？

その鍵を探すのに時間が取られて、火を消し忘れてしまうかもしれません。もしかしたら「私のパスワードを使っていいからこの資料コピーしておいて！」ということも起こりかねません。
時間がなくて焦ったり、心に余裕がなくなってしまうことで、自分の生活に脆弱性を作るのはもったいない！！

TsukushiSpeakerはそのようななくしものをなくし、日常で慌てる時間を減らしたい。自分の日常に生まれる脆弱性を減らしたい、そのような気持ちから開発しました。

設置したマイクに向かって声で物の名前を言うと、別に設置したカメラが自動で写真を撮ります。

![](https://i.imgur.com/krQmPin.jpg)


物の場所がわからなくなった時にはタブレットから検索し、場所と物を置いた時に撮った写真を表示します。

![](https://i.imgur.com/fZJIyFg.jpg)


(注)2020年12月31日現在
wake wordとして「ラズパイ(らずぱい)」と物の名前を言う前に言い、起動させます。その後物の名前を言う事で、物の名前も保存されます。現時点ではwake wordを言う時点でも写真が撮られてしまうので、合計2枚の写真が保存されます。

## 2. 仕組み(2020_12_29時点)
<!-- もっと技術説明を深くした方が良いかな... -->
> Raspberry Piと音声認識Juliusを利用することによって、スマートスピーカーのようにマイクから声を認識し、辞書機能を使って単語を認識します。
> その認識した時に写真を撮ります。
> 単語と写真をリンクして保存し、あとから確認できるようにします。

`python3 main.py`
と実行コマンド入力後、wake wordである「ラズパイ(らずぱい)」と話しかけます。
![](https://i.imgur.com/uJvn5HA.jpg)

その後、記憶させたい物の名前を話しかけます。
この場合は「めがね」と話しかけています。
![](https://i.imgur.com/bR03jFY.jpg)

そうすると、画像が保存されます。
「眼鏡」が認識され、日時と物の名前の入ったファイル名となり保存されます。
![](https://i.imgur.com/N8RGk1m.jpg)

そのファイルを開くと、眼鏡の置いてある場所が表示されます。
(プロトタイプのカメラが古かったせいか画質は荒い)
![](https://i.imgur.com/2xnaUyY.jpg)


## 3. 準備する物
・コンピュータ(2020_12_29時点ではRaspberry Pi3 ModelB)
・Ubuntu OS(version 20.10)
・USBマイク
・USBカメラ
・ラズパイ用ディスプレイ

## 4. インストール方法(2020_12_29時点)
ぜひ皆さんのおうちにも設置してみてください。
そしてフィードバックお待ちしてます！！
ご質問やフィードバックはTwitter @taarusauce または @labo_4423 までお願いします。

### ・Ubuntu20.10
・下記のコマンドを実行します。  
`sudo apt update`  
`sudo apt upgrade`    
`sudo apt install julius`  
`sudo apt install git`  
`git clone https://github.com/taruscript/TsukushiSpeaker`  
`cd TsukushiSpeaker`  
`sudo apt install python3-pip3`  
`sudo apt install python3-pyaudio`  
`pip3 install -r requirements.txt`  
`pip install numpy`  
`sudo spt install flac`  

<!-- 下記のセットアップしたものをこのディレクトリに配置する。
https://qiita.com/fishkiller/items/dfd1b13a4380c6aa6322 -->

・pip実行時エラーが出た場合はこのコマンドも実行。
`sudo apt install python3-pyaudio`

`sudo apt install fswebcam`

・実行します
`python3 main.py`


### ・Raspberry Pi
Comming Soon

## 5. トラブルシューティング
### 1.マイクを認識しない場合
マイクの優先順位が低い場合があります。
`cat /proc/asound/modules` から確認してください。
### 

## 6. 連絡先
Twitter @taarusauce
または
Twitter @labo_4423
