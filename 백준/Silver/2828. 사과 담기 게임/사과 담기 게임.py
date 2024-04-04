import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())

left = 1
right = M
distance = 0

for i in range(J):
    now = int(sys.stdin.readline())

    if now < left:
        distance += left - now
        left = now
        right = now + M - 1
    elif now > right:
        distance += now - right
        right = now
        left = now - M + 1

print(distance)
