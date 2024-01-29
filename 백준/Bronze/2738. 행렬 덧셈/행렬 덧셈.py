a, b = list(map(int, input().split()))

c, d = [], []

for i in range(a):
    row = list(map(int, input().split()))
    c.append(row)

for i in range(a):
    row = list(map(int, input().split()))
    d.append(row)

for i in range(a):
    for j in range(b):
        print(c[i][j] + d[i][j], end= " ")
    print()

