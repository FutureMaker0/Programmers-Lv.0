def solution(array):
    answer = 0
    
    array.sort()
    # print(array)
    
    mid = len(array) // 2
    
    answer = array[mid]
    
    return answer
