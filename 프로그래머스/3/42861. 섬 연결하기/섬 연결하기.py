#3.사이클X
#2.같은 연결X
#1.비용을 기준으로 정렬
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2]) #2번째 리스트 항목을 기준으로 정렬 -> 암기
    
    #연결되었는지 확인
    visited = set([costs[0][0]])
    
    while len(visited) != n:
        for cost in costs:
            if (cost[0] in visited) and (cost[1] in visited):
                continue
            if (cost[0] in visited) or (cost[1] in visited):
                visited.update([cost[0], cost[1]]) #중복되는 값 삭제
                answer += cost[2]
                break
    
    
    return answer