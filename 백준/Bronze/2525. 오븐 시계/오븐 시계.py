A, B = map(int, input().split())
C = int(input())

total_minutes = (B + C) // 60  # 총 소요 시간을 분 단위로 계산

if total_minutes > 0:
    A = (A + total_minutes) % 24  # 24 시간을 초과하는 경우에 대한 처리
    B = (B + C) % 60
else:
    B = B + C

print(A, B)