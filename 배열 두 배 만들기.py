def solution(numbers):
    # answer = [0] * (len(numbers))
    answer = []
    
    for i in range(len(numbers)):
        answer.append((numbers[i]*2))
    
    return answer
