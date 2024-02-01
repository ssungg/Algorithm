N, M = map(int, input().split())

# 바구니 초기화
baskets = [0] * N

# M번의 공을 넣기
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        baskets[idx] = k

# 결과 출력
print(*baskets)