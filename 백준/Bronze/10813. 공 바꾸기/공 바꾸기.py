n, m = map(int, input().split())
a = []

for x in range(1, n+1):
    a.append(x)

for y in range(m):
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]

print(" ".join(map(str, a)))