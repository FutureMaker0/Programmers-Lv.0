def solution(sides):
    answer = 0
    sides.sort()

    # 배열 안에 수가 제일 큰 수일 때,
    for i in range(1, sides[1]+1, 1):
        if sides[0] + i > sides[1]:
            answer += 1
            
    # 새로운 값이 제일 큰 수일 때,
    for i in range(sides[1]+1, sides[0]+sides[1], 1):
        answer += 1
    
    return answer

# 3 6
# 1. 4, 5, 6
# 2. 8, 7
