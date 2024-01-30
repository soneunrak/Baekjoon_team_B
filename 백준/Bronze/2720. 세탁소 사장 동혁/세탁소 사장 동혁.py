a = int(input())

for i in range(a):
    price = int(input())
    for j in [25, 10, 5, 1]:
        print(price//j, end= " ")
        price = price%j
    print()
