## ★★
'''
from itertools import combinations
# from itertools import permutations

def solution(dots):
    a = [] # 리스트 선언
    
    # 연결 가능한 모든 경우의 수 생성
    for (x1,y1),(x2,y2) in combinations(dots,2):
        # print((x1, y1), (x2, y2)) # 6개
        a.append((y2-y1, x2-x1)) # 기울기를 구하기 위함
    
    print(a) # 기울기 -1/4, 2, 1/5, -1
    
    
    for (x1,y1),(x2,y2) in combinations(a,2):
        # print((x1,y1),(x2,y2))
        if x1/x2 == y1/y2:
            return 1
    return 0
'''

def gradient(dot1, dot2):
    ja = abs(dot1[0] - dot2[0])
    mo = abs(dot1[1] - dot2[1])
    return ja/mo

def solution(dots):
    result = gradient(dots[0], dots[2]) - gradient(dots[1], dots[3])
    
    if result == 0:
        return 1
    return 0
    
    
