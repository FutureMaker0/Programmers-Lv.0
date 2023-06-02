# 데큐와 로테이트를 가지고 푸는 게 좋다.


def solution(numbers, direction):
    answer = []
    
    if direction == "right":
        answer = numbers[-1:] + numbers[:-1]
    else:
        answer = numbers[1:] + numbers[:1]
     
    return answer
