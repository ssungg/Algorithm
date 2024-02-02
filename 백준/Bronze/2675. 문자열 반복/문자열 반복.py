t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    num = len(s)

    for i in range(num):
        print(s[i]*r, end='')
    print()