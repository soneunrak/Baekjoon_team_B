num = []
result = 0
for i in range(5):
    num.append(int(input()))

num.sort()
result = sum(num)/5
print(int(result), num[2], sep="\n")