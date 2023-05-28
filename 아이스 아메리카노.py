def solution(money):
    answer = []
    coffee = 5500
    
    rest = 0
    cnt = 0
    
    cnt = money // coffee
    rest = money % coffee
    
    answer = [cnt, rest]

    return answer
