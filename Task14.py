import math
def p(a):
    count = 0
    check = False
    for i in range (2, (math.ceil(math.sqrt(a))+1)):
        if a%i == 0:
            count = 1
    if (count == 1):
        check = False
    else:
        check = True
    return check
a = int(input())
print(p(a))