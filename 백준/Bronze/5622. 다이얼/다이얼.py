s = input()
s = list(s)
res = 0

for i in s:
    if i in 'ABC':
        res += 3
    elif i in 'DEF':
        res += 4
    elif i in 'GHI':
        res += 5
    elif i in 'JKL':
        res += 6
    elif i in 'MNO':
        res += 7
    elif i in 'PQRS':
        res += 8
    elif i in 'TUV':
        res += 9
    elif i in 'WXYZ':
        res += 10
    elif i in "":
        res += 2
    else:
        res += 11
    
print(res)