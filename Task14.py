import math
a = int(input())
count = 0
for i in range (2, (math.ceil(math.sqrt(a))+1)):
    if a%i == 0:
        count = 1
if (count == 1):
    print("No")
else:
    print("Yes")