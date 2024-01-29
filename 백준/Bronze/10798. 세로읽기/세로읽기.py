a = []
r = ''
for i in range(5):
    a.append(input())

for i in range(15):
    for j in range(5):
        if len(a[j]) > i:
            r += a[j][i]
print(r)
