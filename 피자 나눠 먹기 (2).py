def solution(n):
    answer = 0
    pizza = 6
    
    arr = []
    for i in range(1, n+1):
        if (i*pizza) % n == 0:
            arr.append(i)
            
    answer = min(arr)
            
    return answer
