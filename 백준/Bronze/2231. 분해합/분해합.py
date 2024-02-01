a = int(input())
result = 0
for i in range(1, a+1):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == a:
        print(i)
        break
    elif i == a:
        print(0)
