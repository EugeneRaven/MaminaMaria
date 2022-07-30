import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    #a = a.copy()
    #b = b.copy()
    n = len(a)-1
    def forward():
        for i in range (1, n):
            for j in range(i, n):
                for k in range(n):
                    a[j][k] -= a[i][k]*a[j][i-1]/a[i-1][i-1]
                b[j] -= b[i]*a[j][i-1]/a[i-1][i-1]
            print(a)
            print(b)
    def backward():
        x = numpy.zeros(len(b), dtype=float)
        x[n] = b[n]/a[n][n]
        for i in range (0, n-1, -1):
            for j in range(n-i+2, n):
                c += a[j]*x[j]
                x[i] = (b[i]-c)/a[i][i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4.0],
    [2.0, 1.0, 4.0, 3.0]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print(oob_solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))