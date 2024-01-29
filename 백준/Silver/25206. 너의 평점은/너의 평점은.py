grade = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
rating = ["F", "D0", "D+", "C0", "C+", "B0", "B+", "A0", "A+"]

total = 0
result = 0

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total += b
        result += b * grade[rating.index(c)]

print('%.6f' % (result / total))