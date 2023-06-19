def solution(lines):
    line = [0 for i in range(200)] # initializing
    
    for a, b in lines: # [0, 1] [2, 5] [3, 9]
        
        while a < b:
            line[a+100] += 1 
            a += 1 
            
    return len(list(filter(lambda x: x>=2, line)))


'''
[0, 1]
line[100] = 1
[2, 5]
line[102, 103, 104] = 1
[3, 9]
line[103, 104] = 2, line[105, 106, 107, 108] = 1

len(list(filter(lambda x: x>=2,line)))

'''





'''
-
 ----
   ------ 
[3, 5] = 2
   
--
  --
    ------
0

-----
   ------
 ---------
 [1, 9] = 8
  
'''



