def solution(my_string):
    answer = ''
    
    for char in my_string:
        if char in answer:
            continue
        else:
            answer += char
    
    return answer
