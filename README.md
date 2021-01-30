<!--- sechack 20210125 --->


# TsukushiSpeaker
家の中でのなくしものをなくすための便利な道具、TsukushiSpeaker。

### 目次
1. TsukushiSpeakerとは
2. 仕組み
・登録時
・検索時
・参考
3. 準備する物
4. インストール方法
5. トラブルシューティング
6. 連絡先
7. なぜ"Tsukushi"なのか
8. 参考

## 1. TsukushiSpeakerとは

外出する時に「あれ！家の鍵がない！」と慌てた事はありませんか？

その鍵を探すのに時間が取られて、火を消し忘れてしまうかもしれません。もしかしたら「私のパスワードを使っていいからこの資料コピーしておいて！」ということも起こりかねません。
時間がなくて焦ったり、心に余裕がなくなってしまうことで、自分の生活に脆弱性を作るのはもったいない！！

想定しているユーザーは  
- ワンルームに住んでいてモノの収納場所を忘れてしまう方  
- モノがたくさんあって収納場所が分からなくなるような倉庫を持っている方  
- 忘れものタグや収納場所をメモするのが面倒な方
- モノの場所を書いたメモをなくしてしまう方
- 忘れものタグなどではプライバシーが気になる方  

TsukushiSpeakerはそのようななくしものをなくし、日常で慌てる時間を減らしたい。自分の日常に生まれる脆弱性を減らしたい、そのような気持ちから開発しました。


設置したマイクに向かって声で物の名前を言うと、別の場所に設置したカメラが自動で写真を撮ります。
(デモも本当は全方位撮影出来るカメラを使いたかったのですが、プロトタイプなのでお許しください...) 

![](https://i.imgur.com/krQmPin.jpg)


物の場所がわからなくなった時にはタブレットから検索し、場所と物を置いた時に撮った写真を表示します。

![](https://i.imgur.com/fZJIyFg.jpg)

「やっぱり自分の"もの"の情報が流出したりしたら怖いなぁ...」
TsukushiSpeakerはセキュリティ面についても考えました。TsukushiSpeakerを使用する時はネットワークへの接続が不要なので外部に写真が流出する心配をする必要はありません！

## 2. 仕組み

### 登録時

ターミナルを立ち上げて、
`cd TsukushiSpeaker`
と入力して
`python3 voice_recognition.py`
、別のターミナルを立ち上げて
`cd TsukushiSpeaker`  
`python3 GUI.py`
と実行コマンド入力後、wake wordである「つくし」と話しかけます。
wake wordとして「つくし」と言うことで、TsukushiSpeakerを起動させます。
認識し起動すると音が鳴ります。

次に覚えさせたいモノの名前を言いながら置きます。
(参考動画では「メガネ」と言っています)
モノの名前を認識すると別の音が鳴り、モノを置いている時に写真を撮ります。
その写真はモノの名前、日時と紐づけて保存されます。
GUIにJuliusディクテーションキットで認識した結果を共有し、ディスプレイに登録したモノの名前が通知されます。

TsukushiSpeakerではネットワーク接続をせずに使えるようにするため、用意した環境で音声認識ができるようになっています。音声認識Juliusディクテーションキットを利用することによってスマートスピーカーのような音声認識を実現させました。マイクからの音声をJuliusディクテーションキットの辞書機能を使うことによって単語認識させています。

> Tsukushiは京都大学 河原研究室、及び名古屋工業大学 李研究室で開発された「Juliusディクテーションキット」を利用し、言語モデルは、国立国語研究所の『現代日本語書き言葉均衡コーパス』(BCCWJ)を利用して作成されたものです。  

### 検索時
ディスプレイのタッチパネルなどを使い、検索したいモノの名前を入力します。
ヒットすると、検索したモノの名前を撮影した時の写真が表示されます。
(参考動画ではカメラが古く、画質は荒いです)

### 参考  
https://youtu.be/8j_uSsFOT0U  

## 3. 準備する物
* Raspberry Pi4(推奨)
* USBマイク
* USBカメラ
* スピーカー
* Raspberry Pi用ディスプレイ

## 4. インストール方法
Raspberry Pi4を利用したインストール方法を説明します。

ぜひ皆さんのおうちにも設置してみてください。
そしてフィードバックお待ちしてます！！
ご質問やフィードバックはTwitter [@taarusauce](https://twitter.com/taarusauce) または [@labo_4423](https://twitter.com/labo_4423) までお願いします。

### ・Raspberry Pi4
Raspberry Pi OS version 5.4を使用。
下記のコマンドを実行します。
```
git clone https://github.com/taruscript/TsukushiSpeaker.git
cd TsukushiSpeaker
wget https://github.com/julius-speech/julius/archive/v4.4.2.1.tar.gz
tar xvzf v4.4.2.1.tar.gz
cd julius-4.4.2.1
sudo apt-get install libasound2-dev libesd0-dev libsndfile1-dev
./configure --with-mictype=alsa
make
sudo make install
cd ../
mkdir julius-kit
cd julius-kit
wget https://osdn.net/dl/julius/dictation-kit-v4.4.zip
unzip dictation-kit-v4.4.zip
```
これで話しかけた言葉を認識できる状態になります。  
以下のコマンドを実行することでjuliusの利用テストができます。
```
cd ~/julius/julius-kit/dicration-kit-v4.4/
julius -C main.jconf -C am-gmm.jconf -demo
```
ここからは撮影できるように準備をします
```
cd 
cd TsukushiSpeaker
sudo apt install python3-pyaudio flac fswebcam 
pip3 install -r requirements.txt
```
* TsukushiSpeaker起動  
`python3 voice_recognition.py`  
別のターミナルで下記のコマンドを実行  
`python3 GUI.py`  
その後、ブラウザ（chrome,firefox,edge等）でURL入力欄で
localhost:8000/home.html  
と入力すると画像検索ページが現れます。  

## 5. トラブルシューティング
### 1. マイクを認識しない場合
マイクの優先順位が低い場合があります。
`cat /proc/asound/modules` を入力して確認します。
"snd_usb_audio" 以外のモジュールが0番(最優先)になっている場合には変更が必要なので、以下のコマンドを実行してください。
`sudo vim /etc/modprobe.d/alsa-base.conf`
エディタが開いたら以下の3行を追加してください。
```
options snd slots=snd_usb_audio,snd_bcm2835
options snd_usb_audio index=0
options snd_bcm2835 index=1
```
ターミナルに戻り以下のコマンドを実行してください。
```
sudo vim ~/.profile
export ALSADEV="plughw:0,0"
sudo reboot
```
再起動したらもう一度`cat /proc/asound/modules` で確認してください。

### 2. 他のライブラリーが不足している場合
マイクの認識だけではなく、画像を認識するライブラリーが不足していて動かない場合があります。以下のコマンドを実行してください。
```
sudo apt-get install alsa-utils sox libsox-fmt-all
sudo sh -c "echo snd-pcm >> /etc/modules"
sudo reboot
```

### 3. Raspberry Pi3 ModelBを利用したい場合
Raspberry Pi4と同じようにインストールしてみてください。
Raspberry Pi4よりも非常に動作が重くなりますが、利用可能です。

### 4. Ubuntuの場合

Ubuntu20.10でも使う事ができます。
VMだとマイク設定をしないといけなかったりと、環境にも依るのでご自分の判断でご利用ください。

Ubuntu20.10を起動させます。
下記のコマンドを実行します。  
```bash
sudo apt update
sudo apt upgrade
sudo apt install -y julius git python3-pip python3-pyaudio flac fswebcam
git clone https://github.com/taruscript/TsukushiSpeaker.git
cd TsukushiSpeaker
pip3 install -r requirements.txt
```

<!-- 下記のセットアップしたものをこのディレクトリに配置する。
https://qiita.com/fishkiller/items/dfd1b13a4380c6aa6322 -->

* pip3コマンド実行時にエラーが出た場合は下記も実行  
`sudo apt install python3-pip`

* TsukushiSpeaker起動  
`python3 voice_recognition.py`  
別のターミナルで下記のコマンドを実行  
`python3 GUI.py`  
その後、ブラウザ（chrome,firefox,edge等）でURL入力欄で
localhost:8000/home.html  
と入力すると画像検索ページが現れます。  

さらに、他のLinuxディストリビュージョンでも動作が可能です。その場合は各パッケージに置き換えるなどご自身で対応をお願いします！

## 6. 連絡先
Twitter [@taarusauce](https://twitter.com/taarusauce)
または
Twitter [@labo_4423](https://twitter.com/labo_4423)

## 7. なぜ"Tsukushi"なのか

「またスマホどこに置いたか忘れちゃった〜！"つくし"みたいに、ひょっこり出てこないかなぁ…」
なくしものをした時に誰もが思うことではないでしょうか。

「つくし---Tsukushi」
それはひょっこりと現れ、春の訪れを教えてくれるもの。
雑草ではあるものの、春の季語ともなっていて、人間の生活に親しみがあるもの。
冬の間もスギナは枯れても、土の中で成長する強いもの。

生活に溶け込み、人間が気にかけていない時間も「もの」を記憶し、なくしものをしてしまった時には「ひょっこり」現れるお手伝いをします。そして見つかった時には、まだ寒い春先につくしを見つけた時のようにニコっとなるような、そんなたくましいTsukushiSpeakerが欲しい。
そう考えたからです。

## 8. 参考
* Julius Dictation Kit
https://github.com/julius-speech/dictation-kit

* Raspberry PiとJuliusで特定の単語を認識させる
https://www.pc-koubou.jp/magazine/19743
