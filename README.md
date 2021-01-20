
# TsukushiSpeaker
家の中でのなくしものをなくすための便利な道具、TsukushiSpeaker。

### 目次
1. TsukushiSpeakerとは
2. 仕組み
3. 準備する物
4. インストール方法
・Raspberry Pi4
・Raspberry Pi3 ModelB
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
- モノがたくさんあって収納場所が分からなくなる倉庫を持っている方  
- 忘れものタグや収納場所をメモするのが面倒な方  

TsukushiSpeakerはそのようななくしものをなくし、日常で慌てる時間を減らしたい。自分の日常に生まれる脆弱性を減らしたい、そのような気持ちから開発しました。  

設置したマイクに向かって声で物の名前を言うと、別に設置したカメラが自動で写真を撮ります。(本当は全方位撮影出来るカメラを使いたかったのですが、プロトタイプなのでお許しください...)  
またTsukushiSpeakerを使用するときはネットワークへの接続が不要なので外部に写真が流出する可能性を軽減できます。

![](https://i.imgur.com/krQmPin.jpg)


物の場所がわからなくなった時にはタブレットから検索し、場所と物を置いた時に撮った写真を表示します。

![](https://i.imgur.com/fZJIyFg.jpg)

(注)2021年1月16日現在
wake wordとして「つくし」と物の名前を言う前に言い、起動させます。その後物の名前を言う事で、物の名前で写真が保存されます。

## 2. 仕組み(2021_1_16時点)
wake wordとして「つくし」と物の名前を言う前に言い、起動させます。その後物の名前を言う事で、物の名前で写真が保存されます。

> Raspberry Piと音声認識Juliusを利用することによって、スマートスピーカーのようにマイクから声を認識し、辞書機能を使って単語を認識します。
> その認識した時に写真を撮ります。
> 単語と写真をリンクして保存し、あとから確認できるようにします。

参考：使用動画
https://youtu.be/IYfRbMHzDuA  

`python3 main.py`
と実行コマンド入力後、wake wordである「つくし」と話しかけます。

その後、記憶させたい物の名前を話しかけます。
この場合は「めがね」と話しかけています。

そうすると、画像が保存されます。
「眼鏡」が認識され、日時と物の名前の入ったファイル名となり保存されます。

そのファイルを開くと、眼鏡の置いてある場所が表示されます。
(カメラが古く、画質は荒いです)

またTsukushiは京都大学 河原研究室、及び名古屋工業大学 李研究室で開発された「Juliusディクテーションキット」を利用し、言語モデルは、国立国語研究所の『現代日本語書き言葉均衡コーパス』(BCCWJ)を利用して作成されたものです。  

## 3. 準備する物
* Raspberry Pi4
(Raspberry Pi3 ModelBの場合はUbuntu OS version 20.10をインストール)
* USBマイク
* USBカメラ
* Raspberry Pi用ディスプレイ

## 4. インストール方法(2021_1_16時点)
Raspberry Pi4の場合、Raspberry Pi3 ModelBの場合の2通りを説明します。

ぜひ皆さんのおうちにも設置してみてください。
そしてフィードバックお待ちしてます！！
ご質問やフィードバックはTwitter [@taarusauce](https://twitter.com/taarusauce) または [@labo_4423](https://twitter.com/labo_4423) までお願いします。

### ・Raspberry Pi4
Raspberry Pi OS version 5.4を使用。
下記のコマンドを実行します。
```
mkdir julius
cd julius
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

cd ~/julius/julius-kit/dicration-kit-v4.4/
julius -C main.jconf -C am-gmm.jconf -demo
```
これで話しかけた言葉を認識できる状態になります。
ディレクトリ"julius"の中で以下のコマンドを実行します。
```
git clone https://github.com/taruscript/TsukushiSpeaker.git
cd TsukushiSpeaker
vim julius-start.sh
```
そしてjulius-start.shの中身を以下に変更します。
`julius -C ./julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ./dict/greeting -input mic -module > /dev/null`
保存しターミナルに戻り以下のコマンドを実行します。
```
sudo apt install python3-pyaudio flac fswebcam
pip3 install -r requirements.txt
```
* TsukushiSpeaker起動  
`python3 main.py`  
別のターミナルで下記のコマンドを実行  
`python3 GUI.py`  
その後、ブラウザ（chrome,firefox,edge等）でURL入力欄で
localhost:8000/home.html  
と入力すると画像検索ページが現れます。  

### ・Raspberry Pi3 ModelB
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
`python3 main.py`  
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

### 3. 他のOSなどで失敗する場合
* Raspberry Pi3 ModelBの場合はRasbianでは失敗することが確認されています。
Ubuntu20.10をインストールしてください。

* VMでのUbuntu, Mac OSも失敗することが確認されています。

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
