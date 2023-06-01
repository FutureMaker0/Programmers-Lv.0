def solution(n, numlist):
    answer = []
    
    # numlist.sort()
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    
    return answer
