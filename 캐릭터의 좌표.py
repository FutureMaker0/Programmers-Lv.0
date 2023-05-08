def solution(keyinput, board):
    answer = [0, 0]
    init = [0, 0] # 원점은(0,0)

    for key in keyinput:
        if key == 'left':
            ## abs(init[0]) 4
            ## board[0]//2 = 4 (.5)
            if abs(init[0]-1) > (board[0]//2):
                init[0] = init[0]
            else:
                init[0] -= 1

        '''
        key       left left left left left
        init[0]      0   -1   -2   -3   -4
        init[0]-1   -1   -2   -3   -4   -5
        board[0]//2 -4   -4   -4   -4   -4
        '''
                
        elif key == 'right':
            if init[0] >= (board[0]//2):
                init[0] = init[0]
            else:
                init[0] += 1
        '''
        key       right right right right right
        init[0]       0     1     2     3     4
        board[0]//2   4     4     4     4     4
        '''
        
        elif key == 'up':
            if init[1] >= (board[1]//2):
                init[1] = init[1]
            else:
                init[1] += 1
        
        else:
            if abs(init[1]-1) > (board[1]//2):
                init[1] = init[1]
            else:
                init[1] -= 1
        
        answer = [init[0], init[1]]
        
    return answer
