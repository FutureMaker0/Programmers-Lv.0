import math

# 8 2 1 3
# 24/6 + 2/6 = 26/6 = 13/3

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = 0
    
    lcm = (denom1*denom2)//(math.gcd(denom1,denom2))
    lcm = int(lcm)
    
    numer1 *= (lcm//denom1)
    
    numer2 *= (lcm//denom2)
    
    numer = numer1 + numer2 # 26
    denom = lcm # 6
    gcd = math.gcd(numer, denom)
    
    numer = numer // math.gcd(numer, denom) # 13
    denom = denom // math.gcd(numer*gcd, denom) # 3
    
    answer = [numer, denom]
    
    return answer
    
