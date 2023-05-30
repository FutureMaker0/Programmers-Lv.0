def solution(hp):
    answer = 0
    ant_power = [5, 3, 1]
        
    for power in ant_power:
        if hp >= power:
            answer += (hp//power)
            hp -= ((hp//power)*power)

    return answer
