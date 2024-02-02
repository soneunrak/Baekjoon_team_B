a = int(input())
c = list(map(int, input().split()))

ary = sorted(set(c))

dic = {}
for i in range(len(ary)):
    dic[ary[i]] = i

for i in c:
    print(dic[i],end=" ")