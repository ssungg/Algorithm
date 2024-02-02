l = []
for _ in range(28):
    n = int(input())
    l.append(n)
l.sort()

count = 0
l2  =[]

i = 1

while count < 2:
    if i not in l:
        l2.append(i)
        count += 1
    i += 1
    
print("\n".join(map(str, l2)))