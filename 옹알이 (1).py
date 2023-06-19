'''
정규표현식

aye, ye, woo, ma 으로 조합가능한 문자 찾기

from itertools import permutations
permutations([1, 2, 3, 4], 2)

'''
'''
def solution(babbling):
    answer = 0
    
    for b in babbling:
        # print(b) # aya
        
        for w in ["aya", "ye", "woo", "ma"]: # aya
            if w*2 not in b:
                b = b.replace(w, '-')
                print(w*2, b)
        print(' ')
        
#         if len(b.strip()) == 0:
#             # print(len(b.strip())
#             answer += 1
            
    # return answer
'''

'''
# from itertools import combinations
from itertools import permutations

def solution(babbling):
    answer = []
    can = ["aya", "ye", "woo", "ma"]
    
    # for case in can:
    # print(list(permutations(can, 2)))
    
    temp = ''
    for k in list(permutations(can, 2)):
        # print(k, len(k))
        
        for i in range(len(k)):
            temp += k[i]
        # print(temp)
        answer.append(temp)
        temp = ''
    print(answer)
        
    
    cnt = 0
    for case in answer:
        for b in babbling:
            if b in case:
                cnt += 1
    
    return cnt
'''


# from itertools import combinations
from itertools import permutations

def solution(babbling):
    answer = []
    can = ["aya", "ye", "woo", "ma"]
    
    # for case in can:
    # print(list(permutations(can, 2)))
    
    list0 = list(permutations(can, 1))
    list1 = list(permutations(can, 2))
    list2 = list(permutations(can, 3))
    list3 = list(permutations(can, 4))
    final_list = []
    
    # final_list.append(list0).append(list1).append(list2).append(list3)
    final_list.append(list0)
    final_list.append(list1)
    final_list.append(list2)
    final_list.append(list3)
    # print(final_list)
    
    temp = ''
    answer2 = []
    
    for lists in final_list:
        # print(lists)
        for case_of_lists in lists:
            for i in range(len(case_of_lists)):
                temp += case_of_lists[i]
            
            # print(temp)
            answer2.append(temp)
            temp =''
        # print(' ')
        
    # print(answer2)
    
    cnt = 0
    for case in answer2:
        for b in babbling:
            if b == case:
                cnt += 1
    
    return cnt
    
    
    
    '''
    temp = ''
    for k in list(permutations(can, 2)):
        # print(k, len(k))
        
        for i in range(len(k)):
            temp += k[i]
        # print(temp)
        answer.append(temp)
        temp = ''
    print(answer)
        
    
    cnt = 0
    for case in answer:
        for b in babbling:
            if b in case:
                cnt += 1
    
    return cnt
    '''

