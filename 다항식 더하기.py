'''
일단 3개가 보이는군요.

0으로 시작하는 수는 없습니다. x의 계수가 0이면 그냥 x를 없애면 됩니다. - clear
계수 1은 생략합니다. x의 계수가 1이면 1x가 아닌 x로 반환하시면 됩니다. - clear
0 < polynomial에 있는 수 < 100. x의 계수가 10이 넘어갈 수 있으므로 이 점 유의하시고 다시 풀어보세요.
'''

def solution(polynomial):
    # answer = ''
    
    temp = []
    for hang in polynomial.split(' + '):
        if hang == 'x':
            hang = hang.replace('x', '1x')
            temp.append(hang)
        else:
            temp.append(hang)
    
    gyesu = 0
    rest = 0  
    for hang2 in temp:    
        if 'x' in hang2:
            gyesu += int(hang2[:-1])
        else:
            rest += int(hang2)
    
    if gyesu == 0 and rest == 0:
        return ""
    elif gyesu == 0 and rest > 0:
        return f'{rest}'
    elif gyesu == 1 and rest == 0:
        return f'x'
    elif gyesu == 1 and rest > 0:
        return f'x + {rest}'
    elif gyesu > 1 and rest == 0:
        return f'{gyesu}x'
    elif gyesu > 1 and rest > 0:
        return f'{gyesu}x + {rest}'
    
