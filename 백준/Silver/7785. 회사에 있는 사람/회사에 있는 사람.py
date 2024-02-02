import sys
n = int(input())
dic = {}

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b == "enter":
        dic[a] = 0
    else:
        del dic[a]

for people in sorted(dic, reverse=True):
    print(people)