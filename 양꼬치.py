def solution(n, k):
    meat = 12000
    drink = 2000
    answer = 0
    
    if n//10 >= 1:
        k -= (n//10)
    
    answer = (n * meat) + (k * drink)
    
    return answer
