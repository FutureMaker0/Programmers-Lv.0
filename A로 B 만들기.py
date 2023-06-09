def solution(before, after):
    answer = 0
    
    for char in before:
        # print(char, end=' ')
        print(before.count(char), end=' ')
        print(after.count(char), end=' ')
        
        if before.count(char) == after.count(char):
            answer = 1
        else:
            answer = 0
            break
    
    return answer
