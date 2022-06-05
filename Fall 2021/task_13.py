def nod(a,b):
    if b==0:
        return (a, 1, 0)
    (d, x, y) = nod(b, a%b)
    return (d, y, x- (a//b)*y)
a = int(input())
b = int(input())
print(nod(a,b))
