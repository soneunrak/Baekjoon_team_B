a = str(input())
b = [-1] * 26
for i in a:
    b[ord(i)-97] = a.index(i)

for i in b:
    print(i,end=" ")