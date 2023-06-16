def solution(score):
    answer = []
    answer3 = []
    
    for set in score:
        avg = (set[0] + set[1]) / 2
        answer.append(avg)

    answer2 = sorted(answer, reverse=True)
    
    for i in answer:
        answer3.append(answer2.index(i)+1)
            
    return answer3
