n, m = map(int, input().split())
arr1 = []
arr2 = []
res = [[0] * m for _ in range(n)]

for _ in range(n):
    a = list(map(int, input().split()))
    arr1.append(a)

for _ in range(n):
    b = list(map(int, input().split()))
    arr2.append(b)

for i in range(n):
    for j in range(m):
        res[i][j] = arr1[i][j] + arr2[i][j]

for p in res:
    print(' '.join(map(str, p)))