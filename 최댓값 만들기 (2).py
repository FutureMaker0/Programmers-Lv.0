def solution(numbers):
    
    numbers.sort()
    
    plus_max = numbers[-1] * numbers[-2]
    minus_max = numbers[0] * numbers[1]
    
    if minus_max > plus_max:
        return minus_max
    return plus_max

    
