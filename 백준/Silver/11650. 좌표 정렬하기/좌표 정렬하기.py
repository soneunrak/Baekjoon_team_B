n = int(input())
ary = []

for i in range(n):
    [x, y] = map(int, input().split())
    ary.append([x, y])
ary.sort()

for i in ary:
    print(i[0], i[1])
