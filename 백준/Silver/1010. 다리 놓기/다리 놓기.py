import sys

def factorial(n):
    if n > 1:
        return (n * factorial(n-1))
    else :
        return 1

T = int(sys.stdin.readline())

for i in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))
    print(factorial(M) // (factorial(M-N) * factorial(N)))