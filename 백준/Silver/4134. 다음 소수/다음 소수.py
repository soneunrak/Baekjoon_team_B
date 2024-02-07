import sys

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

a = int(sys.stdin.readline())
for _ in range(a):
    n = int(sys.stdin.readline())
    while True:
        if prime(n):
            print(n)
            break
        else:
            n += 1