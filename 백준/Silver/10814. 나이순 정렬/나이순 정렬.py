import sys
n = int(input())
c = []
for i in range(n):
    [a, b] = list(map(str,sys.stdin.readline().split()))
    c.append([int(a), b])

c.sort(key=lambda x: x[0])
for i in c:
    print(i[0], i[1])
