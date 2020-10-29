"""
    运算符重载
"""


class Vector():
    def __init__(self, i=0, j=0, k=0):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"({self.i}, {self.j}, {self.k})"

    def __add__(self, other):
        i = self.i + other.i
        j = self.j + other.j
        k = self.k + other.k
        return Vector(i, j, k)

    def __sub__(self, other):
        i = self.i - other.i
        j = self.j - other.j
        k = self.k - other.k
        return Vector(i, j, k)

    def __iadd__(self, other):
        self.i += other.i
        self.j += other.j
        self.k += other.k
        return self

    def __isub__(self, other):
        self.i -= other.i
        self.j -= other.j
        self.k -= other.k
        return self


a = Vector(1, 2, 3)
b = Vector(2, 3, 4)

print(a + b)
a += b
print(a)
a -= b
print(a)
