def solution(num, k):
    answer = 0
    not_exist = -1
    num = str(num)
    
    for digit in num:
        print(int(digit))
        
        if int(digit) == k:
            answer = num.index(digit) + 1
            break
        
        else:
            answer = not_exist
        
    return answer
