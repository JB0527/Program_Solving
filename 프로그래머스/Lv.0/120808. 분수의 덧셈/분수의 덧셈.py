import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = denom1*numer2 + denom2*numer1
    gcd= math.gcd(numer,denom)
    answer.append(numer//gcd)
    answer.append(denom//gcd)
    return answer