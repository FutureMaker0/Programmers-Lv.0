def solution(array, n):
    # print(sorted(array, key=lambda x:(abs(x-n),x-n))[0])
    return sorted(array, key=lambda x:(abs(x-n),x-n))[0]

'''
★★
abs(array[i] - n), array[i] - n
'''
