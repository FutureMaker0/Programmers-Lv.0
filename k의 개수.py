def solution(i, j, k):
    '''
    # answer = str([num for num in range(i, j+1)]).count(str(k))  
        
    answer = 0
    for num in range(i, j+1):
        answer += str(num).count(str(k))
    
    return answer
    '''
def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
    





