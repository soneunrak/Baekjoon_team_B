import sys

x,y = map(str, sys.stdin.readline().split())

X = x[::-1]
Y = y[::-1]

z = str(int(X)+int(Y))
print(int(z[::-1]))
