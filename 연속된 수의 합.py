def solution(num, total):
    answer = []
    avg = total // num
    
    if num % 2 != 0:
        for i in range(num):
            answer.append(avg+i)   
        for i in range(num):
            answer[i] -= (num//2)
            
    else:
        for i in range(num):
            answer.append(avg+i)
        for i in range(num):
            answer[i] -= (num//2 - 1)
            
    return answer

'''
6 17 - [2, 3, 4, 5, 6, 7] - [1, 2, 3, 4, 5, 6] - [0, 1, 2, 3, 4, 5] x
4 18 - [3, 4, 5, 6]
7 21 - [3, 4, 5, 6, 7, 8, 9] - [0, 1, 2, 3, 4, 5, 6]

4 14 - [3, 4, 5, 6] - [2, 3, 4, 5] -1
4 18 - [4, 5, 6, 7] - [3, 4, 5, 6] -1
6 27 - [4, 5, 6, 7, 8, 9] - [2, 3, 4, 5, 6, 7] -2
8 36 - [4, 5, 6, 7, 8, 9, 10, 11] - [1, 2, 3, 4, 5, 6, 7, 8] -3

3 - 1
5 - 2
7 - 3

 2 - 0
 4 - 1
 6 - 2
 8 - 3
10 - 4
12 - 5

0 1 2 3  4  5
2 4 6 8 10 12 

2(num+1)
8 / 2 - 1 = 3


'''



