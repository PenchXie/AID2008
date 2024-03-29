def func01(list_target):
    print(list_target)  # [1,2,3]


def func02(*args):
    print(args)  # (1, 2, 3)


def func03(*args, **kwargs):
    print(args)  # (1, 2, 3)
    print(kwargs)  # {a: 4, b: 5, c: 6}


def func04(p1, p2, *, p4, **kwargs):
    print(p1)  # 10
    print(p2)  # 20
    print(p4)  # 30
    print(kwargs)  # {p5: 40}


func01([1, 2, 3])
func02(*[1, 2, 3])
func03(1, 2, 3, a=4, b=5, c=6)
func04(10, 20, p4=30, p5=40)
