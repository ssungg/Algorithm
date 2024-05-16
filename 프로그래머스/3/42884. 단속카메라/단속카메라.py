def solution(routes):
    answer = 0
    
    routes.sort()
    
    cam = -30000
    count = 0
    
    for start, end in routes:
        if start > cam:
            count += 1
            cam = end
        elif end < cam:
            cam = end
    
    answer = count
    return answer