import sys
board = []
result =[]

n,m= map(int, sys.stdin.readline().split())

for i in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    if board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'B':
                        w += 1
                    if board[k][l] != 'W':
                        b += 1
        result.append(min(w ,b))

print(min(result))