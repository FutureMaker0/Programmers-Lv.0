def solution(n):
    answer = 0
    
    # 1 2 3 4 5 6  7  8 9  10 11 12 13 14 15
    # 1 2 4 5 7 8 10 11 14 16 17 19 20 22 25
    
    for i in range(n):
        answer += 1
        while answer%3==0 or '3' in str(answer):
            answer += 1
                
    return answer
