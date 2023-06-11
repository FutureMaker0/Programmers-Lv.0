def solution(s):
    answer = 0
    stack = []
    
    # for i in s.split():
        # print(i, type(i))
        
    for num in s.split(' '):
        try:
            stack.append(int(num))
        except:
            stack.pop()
            
    answer = sum(stack)
    
    return answer
