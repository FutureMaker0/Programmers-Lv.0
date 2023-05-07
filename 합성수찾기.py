'''
<!DOCTYPE html>
<html lang="ko-KR">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>선택자</title>
    <style>
        *{border: 2px solid rgb(156, 119, 192);}
        [id="text"]{border: 2px solid red;}
        input[type="email"]{border:  1px solid saddlebrown;}
    </style>
    '''

n = int(input())
def solution(n):
    answer = 0
    for i in range(1, n+1): # <label for="text">text</label>
        cnt = 0
        for j in range(1, i+1): # <input type="email" id="eamil">email<br>
            if i%j==0: # <label for="text">text</label>
                cnt += 1 # <input type="email" id="eamil">email<br>
                if cnt >= 3:
                    answer += 1
                    break        
    return answer # <label for="text">text</label>
print(solution(n))
'''
</head>
<body>
  <div>
    <h1 class="hi">Hello</h1><p class="123">Hello</p>
    <p class="hi">hello</p><button type="button">Hello</button>
    
    <label for="text">text</label>
    <input type="text" id="text"><br>

    <label for="email">email</label>
    <input type="email" id="eamil">email<br>
    
  </div>
</body>
</html>
'''
