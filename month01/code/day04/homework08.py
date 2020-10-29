"""
    赌大小游戏
"""
from random import randint

# 初始身家
gold = 10000

# while True:
while gold > 0:
    # 玩家下注
    bet = int(input("少侠请下注:"))
#     如果下注金额大于目前金额则返回
    if bet > gold:
        print("超出了你的身家，请重新投注")
        continue
    # 双方下注
    player = randint(1, 6)
    host = randint(1, 6)
    # 报告点数情况
    print("你摇出了%d点,庄家摇出了%d点" % (player, host))
    # 根据点数大小身家变化
    if player > host:
        gold += bet
        print("恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d" % (gold))
        # continue
    elif player == host:
        print("打平了，少侠，在来一局？")
        # continue
    else:
        gold -= bet
        print("少侠,你输了，身家还剩%d" % (gold))
    # gold <= 0时破产, 无法继续游戏
    # if gold == 0:
    #     print("哈哈哈，少侠你已经破产，无资格进行游戏")
    #     break
# 可能退出循环只会因为没钱, 因此无需写else表示互斥性
print("哈哈哈，少侠你已经破产，无资格进行游戏")
