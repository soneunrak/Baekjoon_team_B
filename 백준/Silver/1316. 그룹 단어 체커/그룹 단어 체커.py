a = int(input())
answer = a
for i in range(a):
    word = str(input())
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            answer -= 1
            break

print(answer)