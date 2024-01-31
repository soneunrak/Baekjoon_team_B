a = int(input())
b = int(input())
num = []
for i in range(a, b+1):
    cnt = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            num.append(i)

if len(num) > 0:
    print(sum(num), min(num), sep='\n')
else:
    print(-1)