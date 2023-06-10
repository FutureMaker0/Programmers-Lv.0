from collections import Counter

def solution(s):
    answer = ''
    
    for i, j in Counter(s).items(): # items는 튜플로 반환
        print(i, j)
        if j == 1:
            answer += i
    
    return ''.join(sorted(answer))
    # return answer
    
