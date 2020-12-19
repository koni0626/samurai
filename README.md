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
cd /home/konishi/samurai/SamurAI-Dig-Here-2020-21/manager
./manager ../samples/sample.dighere ../samurai/samurai.sh ../samurai/samurai.sh../samurai/dog.sh ../samurai/dog.sh> ../samples/test.dighere
```
上記のmanagerコマンドを実行すると、プレイヤー1,プレイヤー2、ともに同じプログラムで対戦します。
../samples/sample.dighereはマップの設定ファイルです。
マップの設定ファイルは自分で作ることができます。
作り方に関しては
/konishi/samurai/SamurAI-Dig-Here-2020-21/documents/manager-jp.htmlの2.1を参照してください。


# ソースコードの解説
## gameInfo.py
ゲームマネージャーからターンごとに情報を取得するクラスです。

## samurai.py
侍を自動操作するプログラムです。乱数で適当に動く予定だったけど、エラーの行動をすると止まってしまうため、何も動かないようにしている。
本プログラムを改造してください。

## dog.py
犬を自動操作するプログラムです。乱数で適当に動く予定だったけど、エラーの行動をすると止まってしまうため、何も動かないようにしている。
本プログラムを改造してください。

## samurai.sh
samurai.pyを起動するためのシェルスクリプトです。
./managerのコマンドの引数に指定します。

## dog.sh
dog.pyを起動するためのシェルスクリプトです。
./managerのコマンドの引数に指定します。

# 実行の仕方

```
./manager ../samples/sample.dighere ../samurai/samurai.sh ../samurai/samurai.sh ../samurai/dog.sh ../samurai/dog.sh> ../samples/test.dighere
```
を実行する。
実行すると、../samples/test.dighereにログが吐かれる。
次に、SamurAI-Dig-Here-2020-21\webpage\dighere.htmlを起動すると、ビューワーが表示される。
ビューワーの上の真ん中あたりに地球みたいなボタンがあるので、クリックする。
ファイルのインポートができるので、../samples/test.dighereを指定すると、ログが可視化される。
なお、サンプルプログラムは一切行動しないようにしているので、全く動かなければ正しく動作している。
