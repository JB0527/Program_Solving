def solution(a, b):
    p = str(a)+str(b)
    q = 2*a*b
    if int(p)>=q:
        answer = int(p)
    else:
        answer = q
    
    return answer