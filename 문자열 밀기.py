
import collections

def solution(A, B):
    if A == B:
        return 0
    
    q = collections.deque(A)
    
    for i in range(len(A)):
        q.rotate(1)
        # print(q)
        if ''.join(q) == B:
            return i+1
        
    return -1

# rotate를 위한 deque 활용

'''
import queue

def solution(A, B):
    if A == B:
        return 0
    
    q = queue.Queue(A)
    for i in range(len(A)):
        q.rotate(1)
        if ''.join(q) == B:
            return i+1
        return -1
'''
# queue도 rotate가 안된다.

