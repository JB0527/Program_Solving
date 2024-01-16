def solution(n, k):
    answer = []
    D = n//k
    for i in range(D):
        answer.append((i+1)*k)
    return answer