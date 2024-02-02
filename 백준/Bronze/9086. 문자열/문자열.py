t = int(input())
res = 0

for _ in range(t):
    a = input()
    a = list(a)
    res = a[0] + a[-1]
    print(res)