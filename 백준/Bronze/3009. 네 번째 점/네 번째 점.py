x_num = []
y_num = []
for i in range(3):
    x, y = map(int, input().split())
    x_num.append(x)
    y_num.append(y)

for i in range(3):
    a = x_num.count(x_num[i])
    b = y_num.count(y_num[i])
    if a == 1:
        c = x_num[i]
    if b == 1:
        d = y_num[i]
print(c, d)