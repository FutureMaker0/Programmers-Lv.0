def solution(common):
    answer = 0
    
    if common[0] != 0:
        d = common[2] - common[1]
        r = common[2] // common[1]
    else:
        d = common[2] - common[1]

    # 등차수열인지, 등비수열인지 먼저 판별
    
    # 등차수열
    if common[2] == common[0] + (2)*d:
        return common[-1] + d

    # 등비수열
    elif common[2] == common[0] * r**(2):
        return common[-1] * r

    
# 등비수열 첫 항이 0일 때의 문제.
