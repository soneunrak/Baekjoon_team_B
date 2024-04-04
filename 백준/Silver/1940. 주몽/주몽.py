import sys

N = int(input())
M = int(input())

A = sorted(list(map(int, sys.stdin.readline().split())))
left, right = 0, N-1
cnt = 0

while left < right:
    result = A[left] + A[right]
    if result < M:
        left += 1
    elif result > M:
        right -= 1
    elif result == M:
        cnt += 1
        left += 1
        right -= 1

print(cnt)