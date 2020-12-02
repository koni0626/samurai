# coding:UTF-8
import sys

class GameInfo:
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.agent_number = 0
        self.stadium_size = 0
        self.step = 0
        self.max_step = 0
        self.hole_list = []
        self.public_moneys_list = []
        self.new_money_list = []
        self.agent_pos_list = []
        self.action_plan_list = []
        self.action_list = []
        self.my_score = 0
        self.enemy_score = 0
        self.remain_money = 0
        self.remain_time = 0
    
    # ゲームマネージャーからの情報取得(ターンごとにクラスを生成し直すこと)
    def read_game_info(self):
        self.reset()

        self.read_agent_number()
        self.read_stadium_size()
        self.read_step()
        self.read_max_step()
        self.read_holes()
        self.read_public_moneys()
        self.read_new_moneys()
        self.read_agent_pos()
        self.read_action_plan()
        self.read_action()
        self.read_score()
        self.read_remain_money()
        self.read_remain_time()

    def dump(self, filename):
        with open(filename, 'a') as f:
            f.write("agent_number:{}\n".format(self.agent_number))
            f.write("stadium size:{}\n".format(self.stadium_size))

            for i, record in enumerate(self.hole_list):
                f.write("hole{}:({},{})\n".format(i, record[0], record[1]))

            for i, record in enumerate(self.public_moneys_list):
                f.write("public_money{}:pos({},{}) money:{}\n".format(i, record[0], record[1], record[2]))

            for i, record in enumerate(self.new_money_list):
                f.write("new_money{}:pos({},{}) money:{}\n".format(i, record[0], record[1], record[2]))

            for i, record in enumerate(self.agent_pos_list):
                x = record[0]
                y = record[1]
                f.write("agent{} pos:({}, {})\n".format(i, x, y))
            
            for i, record in enumerate(self.action_plan_list):
                f.write("action_plan{}:{}\n".format(i, record))
            
            for i, record in enumerate(self.action_list):
                f.write("action{}:{}\n".format(i, record))
        
            f.write("my_score:{}\n".format(self.my_score))
            f.write("enemy_score:{}\n".format(self.enemy_score))
            f.write("remain_money:{}\n".format(self.remain_money))
            f.write("remain_time:{}\n".format(self.remain_time))
    

    # 自分の番号
    def read_agent_number(self):
        self.agent_number = int(input())
        #print("agent:{}".format(self.agent_number), file=sys.stderr)
    
    # 競技場のサイズ
    def read_stadium_size(self):
        self.stadium_size = int(input())
        #print("stadium_size:{}".format(self.stadium_size), file=sys.stderr)
    
    # 現在のステップ数
    def read_step(self):
        self.step = int(input())
        #print("step:{}".format(self.step), file=sys.stderr)
    
    # 最大ステップ数
    def read_max_step(self):
        self.max_step = int(input())
        #print("max_step:{}".format(self.max_step), file=sys.stderr)

    # 穴の数
    def read_holes(self):
        record = list(map(int, input().split()))
        #print("holes:{}".format(record), file=sys.stderr)
        hole_num = record[0] #穴の数

        for i in range(1, hole_num, 2):
            x = record[i]
            y = record[i + 1]
            self.hole_list.append([x, y])
    
    # 公知の埋蔵金
    def read_public_moneys(self):
        record = list(map(int, input().split()))
        #print("read_public_moneys:{}".format(record), file=sys.stderr)
        num = record[0] #公知の埋蔵金
        for i in range(1, num, 3):
            x = record[i]
            y = record[i + 1]
            money = record[i + 2]
            self.public_moneys_list.append([x, y ,money])
    
    # 犬が感知した埋蔵金
    def read_new_moneys(self):
        record = list(map(int, input().split()))
        #print("read_new_moneys:{}".format(record), file=sys.stderr)
        num = record[0] # 新しく見つかった埋蔵金の数
        for i in range(1, num, 3):
            x = record[i]
            y = record[i + 1]
            money = record[i + 2]
            self.new_money_list.append([x, y ,money])
    
    # エージェントの位置
    def read_agent_pos(self):
        record = list(map(int,input().split()))
        #print("read_agent_pos:{}".format(record), file=sys.stderr)
        for i in range(0, 4, 2):
            x = record[i]
            y = record[i + 1]
            self.agent_pos_list.append([x, y])
    
    # 直前ステップのプレイプラン
    def read_action_plan(self):
        record = list(map(int, input().split()))
        #print("read_action_plan:{}".format(record), file=sys.stderr)
        for i in range(4):
            self.action_plan_list.append(record[i])

    # 直前ステップの行動    
    def read_action(self):
        record = list(map(int, input().split()))
        #print("read_action:{}".format(record), file=sys.stderr)
        for i in range(4):
            self.action_list.append(record[i])

    # スコア
    def read_score(self):
        record = list(map(int, input().split()))
        #print("read_score:{}".format(record), file=sys.stderr)
        self.my_score = record[0]
        self.enemy_score = record[1]
    
    # 残りの埋蔵金
    def read_remain_money(self):
        self.remain_money = int(input())
        #print("read_remain_money:{}".format(self.remain_money), file=sys.stderr)
    

    # 残りの時間
    def read_remain_time(self):
        self.remain_time = int(input())
        #print("read_remain_time:{}".format(self.remain_time), file=sys.stderr)
    



