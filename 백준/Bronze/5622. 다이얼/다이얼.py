a = str(input())
result = 0
for word in a:
    if word in "ABC":
        result = result+3
    elif word in "DEF":
        result = result+4
    elif word in "GHI":
        result = result+5
    elif word in "JKL":
        result = result+6
    elif word in "MNO":
        result = result+7
    elif word in "PQRS":
        result = result+8
    elif word in "TUV":
        result = result+9
    elif word in "WXYZ":
        result = result+10
    elif word in "":
        result = result+2

print(result)
