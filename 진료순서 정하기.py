def solution(emergency):
    answer = []
    
    emergency_2 = sorted(emergency, reverse = True)
    
    for case in emergency:
        answer.append(emergency_2.index(case) + 1)
    
    return answer
