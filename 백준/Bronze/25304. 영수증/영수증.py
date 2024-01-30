price = int(input())
n = int(input())
res = 0

for i in  range(n):
    p, num = map(int, input().split())
    res = res + p*num

if price == res:
    print("Yes")
else:
    print("No")