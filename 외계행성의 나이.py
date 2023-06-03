def solution(age):
    answer = ''
    
    # int(i) + 97 더해서 알파벳 값을 찾는다
    # chr로 바꿔서 실제 형변환 해준다
    # str로 감싸서 이어붙일 수 있는 상태로 만들어준다
    # answer에다가 이어붙여준다.
    
    for i in str(age):
        answer += str(chr((int(i) + 97)))
    
    return answer
