def solution(n):
    answer = 0
    pizza = 7
    temp = n % pizza
    
    if temp == 0:
        answer = n // pizza
        
    elif temp > 0 and temp < pizza - 1:
        answer = (n // pizza) + 1
    
    return answer
