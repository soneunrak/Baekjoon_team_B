p, n = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse=True)
print(c[n-1])