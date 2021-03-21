"""
一副扑克牌52张（除了大小王），4个玩家在玩，模拟系统发牌、洗牌和整理牌，具体需求如下：
【1】先按照顺序打印出一副扑克牌
【2】在没有洗牌的情况下，输出发到四个玩家的扑克牌
【3】实现对扑克牌的洗牌，然后输出发到四个玩家的扑克牌
【4】对于洗牌后的四个玩家的扑克牌进行整理
整理规则1：数字从小到大（3、4、5、6、7、8、9、10、J 、Q、K、A、2）
整理规则2：在数字相同的情况下，按照花色（黑、红、梅、方）的顺序
====================================================
扑克牌游戏开始.....
请选择要执行的操作【1-生成牌 2-打印牌  3-发牌  4-洗牌  5-整理牌  6-退出】

"""
import time
import random
POKER_DICT = {
    'number': ("3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"),
    'type': ('♣', '♥', '♦', '♠')

}

class PokerGame:
    def __init__(self, poker_number: int = 1, person_number: int = 4):
        self.poker_number = poker_number  # 几副牌
        # 定义存储变量
        self.poker_list = []
        # 玩家人数
        self.person_number = person_number  
        # 定义集合存储玩家的牌
        self.person_poker_list = []
        # self.person_sorted_poker_list = []

    def start(self):
        print('游戏正在启动.....')
        # time.sleep(2)
        print('游戏已启动！！')
        print('='*30 + '扑克牌游戏开始' + '='*30)
        while True:
            input_number = input(
                '请选择要执行的操作【1-生成牌 2-打印牌 3-打印玩家的牌 4-发牌  5-洗牌  6-整理牌  7-退出】：')
            if input_number == '1':
                print('正在生成牌，请稍后..... ')
                # time.sleep(2)
                self.build()
                print('扑克牌已生成')

            elif input_number == '2':
                print('正在打印牌，请稍后.....')
                # time.sleep(2)
                self.print_all_poker(self.poker_list)
                print('扑克牌打印成功')
            elif input_number == '3':
                print('正在打印玩家的牌，请稍后.....')
                # time.sleep(2)
                self.print_person_poker()
                print('扑克牌打印成功')
            elif input_number == '4':
                print('正在发牌中.....')
                # time.sleep(2)
                self.deal_poker()
                print('扑克牌已发好')
            elif input_number == '5':
                print('正在洗牌中.....')
                # time.sleep(2)
                random.shuffle(self.poker_list)
                print('洗牌完毕')
            elif input_number == '6':
                print('正在整理中.....')
                # time.sleep(2)
                self.person_sorted_poker()
                print('整理完毕')
            elif input_number == '7':
                print('游戏退出成功，再见！')
                break
            else:
                print('输入的数字无效，请重新输入')

    # 1-生成牌
    def build(self):
        # 生成扑克牌
        # 定义一个poker数字
        poker_num = []
        for num in range(13):
            poker_num.append('%02d' % num)
        # 定义poker花色
        poker_type = ['00', '01', '02', '03']
        # 生成牌 几副牌==》数字==》花色
        for pair in range(self.poker_number):
            for number in poker_num:
                for num_type in poker_type:
                    self.poker_list.append(number + num_type)
            # print(self.poker_list)

    # 2-打印牌
    def print_all_poker(self, print_list: list):
        # 打印所有的牌
        for one_poker in print_list:
            print("%s%s" % (POKER_DICT['type'][int(
                one_poker[2:])], POKER_DICT['number'][int(one_poker[:2])]), end=' ')
        print()

    # 4-发牌
    def deal_poker(self):
        # [[1],[2],[3],[4]]
        for person_index in range(self.person_number):
            temp_list = []
            for index in range(len(self.poker_list)):
                if index % self.person_number == person_index:
                    # 附加到这个玩家的集合
                    temp_list.append(self.poker_list[index])
            self.person_poker_list.append(temp_list)
        # print(self.person_poker_list)

    # 3-打印玩家的扑克
    def print_person_poker(self):
        for index, val in enumerate(self.person_poker_list):
            # 遍历玩家牌
            print('第%d家的牌:' % (index+1) ,end='')
            self.print_all_poker(self.person_poker_list[index])
            print()
    #6-整理玩家手上的牌
    def person_sorted_poker(self):
        for one_person_poker in self.person_poker_list:
            # print(one_person_poker)
            one_person_poker.sort()    

if __name__ == '__main__':
    obj = PokerGame()
    obj.start()
