class A():
    def func01(self):
        print("A")


class B(A):
    def func01(self):
        print("B")
        super().func01()


class C(A):
    def func01(self):
        print("C")


class D(A):
    def func01(self):
        print(D)


class E(B, C, D):
    def func01(self):
        print("E")
        super().func01()
        super().func01()

e = E()
e.func01()