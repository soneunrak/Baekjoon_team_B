N = int(input())
D = int(input())
A = []
cnt = 0

for i in range(N-1):
   A.append(int(input()))

A.sort(reverse=True)

if N == 1:
   cnt = 0
else:
   while D <= A[0]:
      D += 1
      A[0] = A[0] - 1
      cnt += 1
      A.sort(reverse=True)

print(cnt)