a, b, c = map(int, input().split())
res = 0

if a == b == c:
    res = 10000 + a * 1000
elif a==b:
    res = 1000 + a * 100
elif a==c:
    res = 1000 + a * 100
elif c==b:
    res = 1000 + b * 100
else:
    res = max(a,b,c)*100
    
print(res)