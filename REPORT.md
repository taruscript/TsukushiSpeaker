```
Error: adin_oss: failed to open /dev/dsp
failed to begin input stream
```

というログが出て、動かないという事案が発生した。

https://qiita.com/mooriii/items/e6bd0c8c07ef4c94fa0d

を参考にすると、どうやらカーネルのバージョンが新しいすぎるので動かないらしい・・・

juliusのバージョンによっては動かない環境がありそう？

（現在インスト済みのjuliusのバージョンは、4.4.2）


----------------------------------------------------------------

sudo make uninstall ができなかったため、make install -n のログを参考に、juliusに関係するプログラムを削除した
---------------------------------------------------------------


apt search julius
をしたところ、version 4.2.2のjuliusが配布されていることに気づいた。
すでにインストール済みの、juliusを削除した後に
sudo apt install julius
でjuliusをインストール

python3 main.pyをして、希望の動作をすることを確認
