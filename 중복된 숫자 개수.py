function solution(array, n) {

    // js에는 count() 함수가 없다.
    
    answer = array.filter(v => v == n).length
    
    return answer;
}
