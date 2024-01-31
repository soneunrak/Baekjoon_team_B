a = int(input())

line = 1
while a > line:
    a -= line
    line += 1

if line % 2 != 0:
    x = line - a + 1
    y = a
elif line % 2 == 0:
    x = a
    y = line - a + 1

print(x,'/',y, sep="")
