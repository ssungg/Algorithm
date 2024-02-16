def solution(array):
    answer = 0
    array.sort()
    res = len(array)//2
    answer = array[res]
    return answer