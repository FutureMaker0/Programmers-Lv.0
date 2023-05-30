import math

def solution(n):
    answer = 0
    
    n2 = int(math.sqrt(n))
    
    if math.pow(n2, 2) == n:
        return 1
    else:
        return 2
    
    return answer
