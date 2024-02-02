l = []
for _ in range(10):
    n = int(input())
    l.append(n)

l2 = []
for i in range(10):
    l2.append(l[i]%42)
l2 = set(l2)
print(len(l2))