from collections import Counter

a = input().lower()
cnt = Counter(a)

max_count = max(cnt.values())  # 가장 많이 나타나는 알파벳의 등장 횟수

# 가장 많이 나타나는 알파벳이 여러 개인지 확인
max_chars = [char for char, count in cnt.items() if count == max_count]

if len(max_chars) == 1:
    print(max_chars[0].upper())
else:
    print('?')