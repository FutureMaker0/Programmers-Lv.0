def solution(numlist, n):
    
    answer = sorted(numlist, key = lambda x: (abs(x-n), n-x))
    
    return answer
    

'''
 numlist = 1 2 3 4 5 6
     x-n = -3 -2 -1 0 1 2
     
lambda x: (abs(x-n), x-n)
    1. 조건1: abs(x-n)
    2. 조건2: x-n
    
    조건1을 만족하도록 먼저 정렬을 하고, 같은 값일 때 조건 2로 정렬
         
## abs(x-n) = 3 2 1 0 1 2 -> 0 1 1 2 2 3 = 4 3 5 2 6 1
     ## n-x = 3 2 1 0 -1 -2 -> 0 -1 1 -2 2 3 = 4 5 3 6 2 1

'''
