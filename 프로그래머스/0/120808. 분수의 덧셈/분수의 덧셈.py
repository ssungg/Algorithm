def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def solution(numer1, denom1, numer2, denom2):
    if denom1==denom2:
        res1 = numer1 + numer2
        res2 = denom1
    else:
        res1 = numer1*denom2 + numer2*denom1
        res2 = denom1*denom2
        
    d = gcd(res1, res2)
    res1 //= d
    res2 //= d
        
    answer = [res1, res2]
    return answer