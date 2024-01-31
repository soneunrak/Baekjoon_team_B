a = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in num:
    result = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                result += 1
        if result == 0:
            cnt += 1

print(cnt)
