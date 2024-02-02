n, m = map(int, input().split())
l = []
for x in range(1, n+1):
    l.append(x)

for _ in range(m):
    i, j = map(int, input().split())
    l[i-1:j] = l[i-1:j][::-1]

print(" ".join(map(str, l)))