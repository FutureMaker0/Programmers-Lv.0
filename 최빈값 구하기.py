from collections import Counter
# enumerate()

def solution(array):
    if len(array) == 1:
        return array[0]
    elif len(set(array)) == 1:
        return array[0]
    
    c = Counter(array) # array의 갯수를 아이템별 갯수를 큰 것부터 인덱스 매겨서 dict으로 반환
    
    new_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
    
    if new_c[0][1] == new_c[1][1]:
        return -1
    return new_c[0][0]
    
    
'''
    temp = len(set(array))
    answer = [0] * (temp+1)
    
    for num in array:
        answer[num] += 1
    print(answer)
    
    if answer.count(max(answer)) != 1:
        return -1
    else:
        return max(answer)
''' 
'''
[1, 2, 3, 3, 3, 4] 1 1 3 1 -> 3
      [1, 1, 2, 2] 2 2 -> -1
               [1] 1 -> 1

1. set을 이용해서 array안에 중복되지 않는 항목의 갯수가 몇 개인지 확인한다.
2. 해당 갯수만큼의 리스트를 선언한다.
3. array 숫자를 읽으면서 해당 숫자 answer[index] 에 +1씩 카운트 해준다.
4. max(answer) 출력 - 최빈값이 여러개면 -1 리턴


'''


