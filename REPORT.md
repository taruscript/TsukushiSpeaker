```
Error: adin_oss: failed to open /dev/dsp
failed to begin input stream
```

というログが出て、動かないという事案が発生した。

https://qiita.com/mooriii/items/e6bd0c8c07ef4c94fa0d

を参考にすると、どうやらカーネルのバージョンが新しいすぎるので動かないらしい・・・

juliusのバージョンによっては動かない環境がありそう？

（現在インスト済みのjuliusのバージョンは、4.4.2）
