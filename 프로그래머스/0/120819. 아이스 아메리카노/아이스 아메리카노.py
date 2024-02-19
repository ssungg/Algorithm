def solution(money):
    answer = []
    coffee = money//5500
    answer.append(coffee)
    coin = money - coffee*5500
    answer.append(coin)
    return answer