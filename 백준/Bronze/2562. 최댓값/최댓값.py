number = []
for a in range(0,9):
    i = int(input())
    number.append(i)
print(max(number))
print(number.index(max(number))+1)