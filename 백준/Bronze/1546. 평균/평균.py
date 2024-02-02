n = int(input())
l = []
l.extend(map(int, input().split()))
score = []
m = max(l)
for i in range(n):
    score.append(l[i]/m*100)

print(sum(score)/n)