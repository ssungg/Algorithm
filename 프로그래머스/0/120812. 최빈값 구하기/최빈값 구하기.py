from collections import Counter

def solution(array):
    answer = 0
    count = Counter(array)
    res = max(count.values())
    answer =  [num for num, cnt in count.items() if cnt == res]

    if len(answer) == 1:
        return answer[0]
    else:
        return -1