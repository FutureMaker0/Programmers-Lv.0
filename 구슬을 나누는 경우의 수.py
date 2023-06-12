## 콤비네이션 조합 문제

def solution(balls, share):
    answer = 0
    mother = 1
    son = 1
    
    for i in range(share):
        mother *= (balls - i)
        son *= (share - i)
    
    # print(mother, son)
    answer = mother / son
    
    return answer
