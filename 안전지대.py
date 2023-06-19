## ★★★ 상

def solution(board):
    n = len(board) # 5
    danger = set() # set선언 - danger
    move = [-1, 0, 1]
    # print(danger)
    
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            
            if x == 0: # x가 비어있으면,
                continue
            else:
                danger.update((i+di, j+dj) for di in move for dj in move)

    cnt = 0
    for (i, j) in danger:
        if 0<=i<n and 0<=j<n:
            cnt += 1
            
    return n*n - cnt
    # return n*n - sum(0<= i <n and 0<= j <n for (i, j) in danger)
    

'''
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
25 - 9 = 16

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 1 0
0 0 0 0 0
25 - 12 = 13

1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
36 - 0 = 36

'''
