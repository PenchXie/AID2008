class Grenade():
    def boom(self, target):
        if isinstance(target, Target):
        # if issubclass(type(target), Target):
            target.damage()
        else:
            raise Exception("你个傻逼在输什么呢")


class Target():
    def damage(self):
        pass

class Enemy(Target):
    def damage(self):
        print("头顶爆字")


class Player(Target):
    def damage(self):
        print("碎屏")


class House(Target):
    def damage(self):
        print("房子塌了")


class Tree(Target):
    def damage(self):
        print("树烧起来了")


class Duck(Target):
    def damage(self):
        print("鸭子熟了")


grenade = Grenade()
enemy01 = Enemy()
player01 = Player()
house01 = House()
tree01 = Tree()
duck01 = Duck()
# abc = 1
grenade.boom(enemy01)
grenade.boom(player01)
grenade.boom(house01)
grenade.boom(tree01)
grenade.boom(duck01)
# grenade.boom(abc)
