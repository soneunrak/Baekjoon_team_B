import sys

ary = []
cnt = 0

for i in range(8):
    ary.append(list(map(str, sys.stdin.readline())))

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if ary[i][j] == 'F':
                cnt += 1

print(cnt)