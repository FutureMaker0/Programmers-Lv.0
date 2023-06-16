def solution(id_pw, db):
    answer = ''

    for set in db:
        if id_pw[0] == set[0] and id_pw[1] == set[1]:
            answer = 'login'

        elif id_pw[0] == set[0] and id_pw[1] != set[1]:
            answer = 'wrong pw'
            
        elif id_pw[0] != set[0] and id_pw[1] != set[1]:
            answer = 'fail'
            
    return answer
