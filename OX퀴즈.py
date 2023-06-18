def solution(quiz):
    answer = []
    result = 0
    
    for ques in quiz:
        temp = ques.split(' = ')
        
        # print(temp)
        # print(temp[0], temp[1], sep=' : ')
        
        result = eval(temp[0])
        # print(result)
        
        if result == int(temp[1]):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer
