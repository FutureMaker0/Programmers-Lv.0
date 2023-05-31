def solution(cipher, code):
    
    # code-1 에서부터 code만큼 뛰면서 값 추출
    return cipher[code-1::code]
    
