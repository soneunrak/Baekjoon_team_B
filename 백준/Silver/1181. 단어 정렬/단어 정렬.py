n = int(input())
words = []
for i in range(n):
    words.append(input())
words_list = set(words)
words = list(words_list)
words.sort()
words.sort(key=len)

for i in words:
    print(i,end="\n")