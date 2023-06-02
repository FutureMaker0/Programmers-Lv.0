def solution(my_string):
    answer = []
    
    for i in my_string:
        # print(i, end=' ')
        try:
            answer.append(int(i))
        except:
            continue
    
    answer.sort()
    
    return answer
