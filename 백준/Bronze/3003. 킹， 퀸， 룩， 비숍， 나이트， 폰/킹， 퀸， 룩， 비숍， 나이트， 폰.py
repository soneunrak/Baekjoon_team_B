a = list(map(int, input().split()))
Chess = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(Chess[i] - a[i], end=" ")