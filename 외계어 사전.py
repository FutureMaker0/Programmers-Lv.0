## ★★
def solution(spell, dic):
    '''
    print(set(spell)) # set은 순서가 무작위
    print(set(dic)) # set은 순서가 무작위
    
    for word in dic:
        if set(spell) == set(word):
            return 1
    return 2
    '''
    
    # print(sorted(spell))
    for word in dic:
        # print(sorted(word))
        if sorted(word) == sorted(spell):
            return 1
    return 2
    
            

'''
o p s
d x z
d m o s
'''
