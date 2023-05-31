# 왜 replace 사용해서는 안되나?

def solution(rsp):
    answer = ''
    
    for i in rsp:
        if i == '2':
            # rsp.replace(i, '0')
            answer += '0'
        elif i == '0':
            # rsp.replace(i, '5')
            answer += '5'
        else:
            # rsp.replace(i, '2')
            answer += '2'
    
    # answer = ''.join(rsp)
    
    return answer
