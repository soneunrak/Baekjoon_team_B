import sys
result = set()
a = str(sys.stdin.readline().strip())

for i in range(len(a)):
    for j in range(i, len(a)):
        result.add(a[i:j+1])

print(len(result))
