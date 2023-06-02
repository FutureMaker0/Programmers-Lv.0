def solution(array):
    answer = []
    
    max_val = max(array)
    idx = array.index(max_val)
    
    answer = [max_val, idx]
    
    return answer
