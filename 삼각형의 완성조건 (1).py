def solution(sides):
    answer = 0
    
    sorted_sides = sorted(sides)
    max_num = max(sides)
    
    # print(sorted_sides)
    print(max_num)
    
    
    if sorted_sides[0] + sorted_sides[1] > max_num:
        answer = 1
    else:
        answer = 2
    
    
    return answer
