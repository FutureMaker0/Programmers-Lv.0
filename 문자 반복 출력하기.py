def solution(my_string, n):
    answer = []
    

    for i in range(len(my_string)):
        for j in range(n):
            answer.append(my_string[i])
    
    return "".join(answer) # 문자열 형태로 return할 떄는 join함수를 이용해서 붙여준다.
    # return answer
