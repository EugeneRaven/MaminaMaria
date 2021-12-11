#from numbers import number - не устанавливается numbers.
# Надеюсь, группа тоже подойдёт.

def table(a,b,c):
    #if isinstance(a, float) and isinstance(b, float) and isinstance(c, float):
    return [[1,a,b], [0,1,c], [0,0,1]]
    #else: - numbers не работает, так что этого пока нет.
        #print("Error")
def multiplication(x,y):
    a = x[0][1] + y[0][1]
    b = x[0][2] + y[0][2] + x[0][1]*y[1][2]
    c = x[1][2] + y[1][2]
    return table(a,b,c)
def inverse(x):
    return [[1,-x[0][1],(x[0][1]*x[1][2]-x[0][2])], [0,1,-x[1][2]], [0,0,1]]
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
x = table(a1,b1,c1)
y = table(a2,b2,c2)
inv1 = inverse(x)
inv2 = inverse(y)
print("Обратная к первой:")
for i in range(3):
    print(*inv1[i])
g = multiplication(x,y)
print("Обратная ко второй:")
for i in range(3):
    print(*inv2[i])
print("Произведение:")
for i in range(3):
    print(*g[i])