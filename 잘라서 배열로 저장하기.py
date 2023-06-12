'''
def solution(my_str, n):
    
    temp = ''
    answer = []
    
    for i in my_str:
        temp += i
        if len(temp) >= n:
            answer.append(temp)
            temp = ''
'''
    
def solution(my_str, n):
    
    answer = []

    for i in range(0, len(my_str), n):
        part = my_str[i:i+n]        
    
        answer.append(part)    
    
    return answer
    
   
