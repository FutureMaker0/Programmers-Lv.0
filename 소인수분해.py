# 252 반례
# 소인수분해는 중복된 항목을 하나로 표기해야하므로 필히 set()을 활용하자.
'''
def solution(n):
    answer = []
    
    for i in range(2, n+1):
        if n >= i:
            if n % i == 0:
                answer.append(i)
                n //= i

    return answer
'''

def solution(n):
    
    d = 2
    s = set()
    # s = []
    while d <= n:
        if n % d == 0:
            # s.append(d)
            s.add(d)
            n /= d
        else:
            d += 1
    
    '''
    answer = set()
    for d in range(2, n+1):
        if n % d == 0:
            answer.add(d)
            n /= d
    '''
    return sorted(list(s))

'''
252 - 2
126 - 2
63 - 3
21 - 3
7 - 7

420 - 2
210 - 2
105 - 3
35 - 5
7 - 7

12 - 2
6 - 2
3 - 3

17 - 17
'''
