import math

def solution(a, b):
    
    temp = []
    for i in a, b:
        i //= math.gcd(a, b)
        temp.append(i)
    # print(temp)    
    
    d = 2
    answer = set()
    while d <= temp[1]:
        if temp[1] % d == 0:
            answer.add(d)
            temp[1] /= d
        else:
            d += 1
    # print(answer)

    if a%b==0 or set(answer) == {2} or set(answer) == {5} or set(answer) == {2, 5}:
        return 1
    return 2

'''
기약분수로 만들었을 때,
분모의 소인수가 2, 5 만으로 구성되면 유한소수이다.
'''
