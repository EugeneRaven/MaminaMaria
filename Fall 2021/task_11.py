# from numbers import number - не устанавливается numbers.
# Надеюсь, группа тоже подойдёт.
class M:
    # Матрицы вида:
    # 1 a b
    # 0 1 c
    # 0 0 1
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        if (self.a == other.a and self.b == other.b and self.c == other.c):
            return True
        else:
            return False

    def table(self, a, b, c):
        # if isinstance(a, float) and isinstance(b, float) and isinstance(c, float):
        return [[1, a, b], [0, 1, c], [0, 0, 1]]
        # else: #- numbers не работает, так что этого пока нет.
        # print("Error")

    def __mul__(self, other):
        a = self.a + other.a
        b = self.b + other.b + self.a * other.c
        c = self.c + other.c
        return [a, b, c]

    def inverse(self):
        a = -self.a
        b = self.a * self.c - self.b
        c = -self.c
        return [a, b, c]


a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
x = M(a1, b1, c1)
y = M(a2, b2, c2)
print("Проверка равенства:")
print(x == y)
v1 = M.inverse(x)
v2 = M.inverse(y)
inv1 = [[1, v1[0], v1[1]], [0, 1, v1[2]], [0, 0, 1]]
inv2 = [[1, v2[0], v2[1]], [0, 1, v2[2]], [0, 0, 1]]
print("Обратная к первой:")
for i in range(3):
    print(*inv1[i])
g = x * y
f = [[1, g[0], g[1]], [0, 1, g[2]], [0, 0, 1]]
print("Обратная ко второй:")
for i in range(3):
    print(*inv2[i])
print("Произведение:")
for i in range(3):
    print(*f[i])
