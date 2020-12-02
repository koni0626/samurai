# coding:UTF-8
import os
import random
from gameInfo import GameInfo


if __name__ == '__main__':
    log_file = "dog.txt"

    if os.path.exists(log_file):
        os.remove(log_file)
    

    gameInfo = GameInfo()
    gameInfo.read_game_info()

    for step in gameInfo.max_step:
        # とりあえず乱数で行動を選択している
        action = random.randint(0, 7)
        # 出力
        print(action)

        # 次のステップの情報を読み込む
        gameInfo.read_game_info()
        gameInfo.dump(log_file)