n = int(input())
c = []
for x in range(0, (n // 3)+1):
    for y in range(0, (n // 5)+1):
        if (x * 3 + y * 5) == n:
            c.append(x+y)

if len(c) > 0:
    print(min(c))
else:
    print(-1)
