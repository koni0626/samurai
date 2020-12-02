#coding:UTF-8
import random
import os
from gameInfo import GameInfo

if __name__ == '__main__':
    log_file = "samurai.txt"

    if os.path.exists(log_file):
        os.remove(log_file)

    gameInfo = GameInfo()

    step = 0
    while True:
        gameInfo.read_game_info()
        gameInfo.dump(log_file)
        #action = random.randint(0, 23)
        # 何もしない
        print(-1)

        step += 1
        if step >= gameInfo.max_step:
            break

        