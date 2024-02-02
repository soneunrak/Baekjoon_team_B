import sys
n = int(input())
ary = []

for i in range(n):
    [x, y] = map(int, sys.stdin.readline().split())
    ary.append([x, y])
ary.sort()

for i in ary:
    print(i[0], i[1])
