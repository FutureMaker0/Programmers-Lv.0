def solution(my_string):
    answer = ''
    
    new_string = []
    for char in my_string:
        char = char.lower()
        new_string.append(char)
        
    new_string.sort()
    
    answer = ''.join(new_string)
    return answer
