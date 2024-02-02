import sys

n = int(input())
ary = []
for i in range(n):
    ary.append(int(sys.stdin.readline()))

ary.sort()
for i in ary:
    print(i)