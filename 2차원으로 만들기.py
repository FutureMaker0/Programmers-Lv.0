def solution(num_list, n):
    answer = []
    
    for _ in range(len(num_list)//n):
        
        # print(num_list[:n]) # n번째까지 list로 반환.
        
        answer.append(num_list[:n])
        num_list = num_list[n:]
    
    return answer



# 0 --> 0 1
# 1 --> 2 3
# 2 --> 4 5
# 3 --> 6 7
