## ★★
from collections import deque

def solution(numbers, k):
    answer = 0
    q = deque(numbers)
    
    if len(numbers) % 2 == 0:
        for _ in range(k-1):
            q.rotate(-2)
        answer = q[0]

    else:
        for _ in range(k-1):
            q.rotate(-2)
        answer = q[0]
        
    return answer


'''
1 2 3 4
3 4 1 2
1 2 3 4

2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2 ## 

3


2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
6 1 2 3 4 5 5
1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4 10
6 1 2 3 4 5
1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3 15



3


2 3 1
3 1 2
1 2 3
2 3 1
3 1 2
1 2 3
2 3 1 ## 
2
'''



