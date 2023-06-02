def solution(my_string, num1, num2):
    
    # 이런거 할려면 리스트로 바꿔줘야 한다.
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    
    answer = ''.join(s)
    # print(answer)
    
    return answer
