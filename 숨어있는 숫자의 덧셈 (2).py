'''
1. findall로 숫자만 뽑아낸다
2. sub로 문자를 +로 바꾼 후 eval('')
3. split 모든 문자 [a-zA-Z] 기준으로 split 해서 sum
'''

'''
def solution(my_string):
    answer = 0
    
    for i in my_string:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            my_string = my_string.replace(i, '-')
            my_string.split('-')
    
    print(my_string)

    return answer

'''
'''
import re

s = "aAb1B2cC34oOp"
re.split('[a-zA-Z]', s)
'''

'''
import re

s = "aAb1B2cC34oOp"
re.sub('[a-zA-Z]', '+', s)

# eval('+++1+2++34+++') 뒤에 +가 있어서 안됩니다.
'''

'''
import re

re.findall('\d+',"aAb1B2cC34oOp9493abcde")
'''

# re import
# findall 함수


import re

def solution(my_string):
    # return sum(map(int, re.findall(r'[0-9]+', my_string))) 
    answer = re.findall(r'\d+', my_string)
    # print(answer)
    
    return sum(int(num) for num in answer)

    
