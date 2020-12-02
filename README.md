# 使い方
samuraiAIが動くだけのサンプルプログラムです。
テスト環境はubuntuです。

[https://github.com/takashi-chikayama/SamurAI-Dig-Here-2020-21.git](https://github.com/takashi-chikayama/SamurAI-Dig-Here-2020-21.git)
から、ゲームマネージャーをクローンしてください。

細かい仕様などは、上記をクローンした後、documentフォルダにあるのでそちらを参照してください。

本サンプルは、上記のゲームマネージャーを以下のパスにクローンした前提で説明します。
**/home/konishi/samurai**

# ゲームマネージャーのクローン
詳細は以下のURLを参照してください。
[https://github.com/takashi-chikayama/SamurAI-Dig-Here-2020-21/tree/master](https://github.com/takashi-chikayama/SamurAI-Dig-Here-2020-21/tree/master)

```
cd /home/konishi/samurai
git clone https://github.com/takashi-chikayama/SamurAI-Dig-Here-2020-21.git
cd SamurAI-Dig-Here-2020-21
make all
make testrun
```

# 本サンプルプログラムのクローン
```
cd /home/konishi/samurai/SamurAI-Dig-Here-2020-21
git clone https://github.com/koni0626/samurai.git
```

# サンプルプログラムの実行
```
./manager ../samples/sample.dighere ../samurai/samurai.sh ../samurai/dog.sh
```

# ソースコードの解説
