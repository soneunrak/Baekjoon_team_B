import sys
dic = {}
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in b:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")