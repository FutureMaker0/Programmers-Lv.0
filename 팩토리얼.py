def solution(n):
    answer = 1
    
    for i in range(1, 20):
        answer *= i
        if answer > n:
            break
        
    answer = i-1

    return answer
