a, b = map(int, input().split())
ary = []
for i in range(1, a+1):
    if a % i == 0:
        ary.append(i)

if len(ary) < b:
    print(0)
else:
    print(ary[b-1])