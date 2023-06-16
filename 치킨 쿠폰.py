def solution(chicken):
    answer = 0
    
    while chicken >= 10:

        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod

    return answer

# 1081
# chi  109  10   1  10 
# mod    1   9   9   0
# ans  108 118 119 120

# chi  108 109  10  10
# mod    1   9   9   0
# ans  108 118 119 120

