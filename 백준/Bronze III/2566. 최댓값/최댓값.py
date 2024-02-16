arr = []
for _ in range(9):
    a = list(map(int, input().split()))
    arr.append(a)

res = 0
r = 0
c = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > res:
            res = arr[i][j]
            r = i
            c = j

print(res)
print(r+1, c+1)