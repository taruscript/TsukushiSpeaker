
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


wake wordとして「つくし」と物の名前を言う前に言い、起動させます。その後物の名前を言う事で、物の名前で写真が保存されます。

## 2. 仕組み
<!-- もっと技術説明を深くした方が良いかな... -->
> Raspberry Piと音声認識Juliusを利用することによって、スマートスピーカーのようにマイクから声を認識し、辞書機能を使って単語を認識します。
> その認識した時に写真を撮ります。
> 単語と写真をリンクして保存し、あとから確認できるようにします。

https://www.youtube.com/watch?v=DdofA4TyYlo&feature=youtu.be  

`python3 main.py`
と実行コマンド入力後、wake wordである「つくし」と話しかけます。

その後、記憶させたい物の名前を話しかけます。
この場合は「めがね」と話しかけています。

そうすると、画像が保存されます。
「眼鏡」が認識され、日時と物の名前の入ったファイル名となり保存されます。

そのファイルを開くと、眼鏡の置いてある場所が表示されます。
(プロトタイプのカメラが古かったせいか画質は荒い)

またTsukushiは京都大学 河原研究室、及び名古屋工業大学 李研究室で開発された「Juliusディクテーションキット」を利用し、言語モデルは、国立国語研究所の『現代日本語書き言葉均衡コーパス』(BCCWJ)を利用して作成されたものです。  

## 3. 準備する物
・コンピュータ(Raspberry Pi3 ModelBを推奨してます)
・Ubuntu OS(version 20.10)
・USBマイク
・USBカメラ
・ラズパイ用ディスプレイ

## 4. インストール方法
ぜひ皆さんのおうちにも設置してみてください。
そしてフィードバックお待ちしてます！！
ご質問やフィードバックはTwitter [@taarusauce](https://twitter.com/taarusauce) または [@labo_4423](https://twitter.com/labo_4423) までお願いします。

### ・Ubuntu20.10
・下記のコマンドを実行します。  
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

・pip3コマンド実行時にエラーが出た場合は下記も実行  
`sudo apt install python3-pip`

・TsukushiSpeaker起動  
`python3 main.py`  
別のターミナルで下記のコマンドを実行  
`python3 GUI.py`  
その後、ブラウザ（chrome,firefox,edge等）でURL入力欄で
localhost:8000/home.html  
と入力すると画像検索ページが現れます。  

### ・Raspberry Pi
Comming Soon

## 5. トラブルシューティング
### 1.マイクを認識しない場合
マイクの優先順位が低い場合があります。
`cat /proc/asound/modules` から確認してください。
### 

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
