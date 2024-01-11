""" 
def solution(cap, n, deliveries, pickups):
    #트럭의 최대 무게 cap
    #n개집
    #최소이동거리
    answer = 0
    #방문할 때 캡이 초과되는 경우
    deliveries.insert(0, 0)
    deliveries.insert(0, 0)
    pickups.insert(0, 0)
    pickups.insert(0, 0)
    for i in range(n):
        if deliveries[-i-1] >= cap:
            A = deliveries[-i-1] % cap
            B = deliveries[-i-1] // cap
            answer += A*(n-i)
            deliveries[-i-2] += B
            if pickups[-i-1] >= cap:
                pickups[-i-1] -= cap
                BB = pickups[-i-1] // cap
                pickups[-i-2] += BB

            elif pickups[-i-1] < cap:
                pickups[-i-1] = 0
                BB = pickups[-i-1] - cap
                pickups[-i-2] += BB        

        elif deliveries[-i-1] < cap:
            answer += 1*(n-i)
            B = deliveries[-i-1] // cap
            deliveries[-i-2] += B
            if pickups[-i-1] >= cap:
                BB = pickups[-i-1] // cap
                pickups[-i-2] += BB

            elif pickups[-i-1] < cap:
                pickups[-i-1] = 0
                BB = pickups[-i-1] - cap
                pickups[-i-2] += BB
   #pickup이 남았을 때
    for j in range(n):
        if pickups[-i-1] >= cap:
            A = pickups[-i-1] % cap
            B = pickups[-i-1] // cap
            answer += A*(n-i)
            pickups[-i-2] += B

        elif pickups[-i-1] < cap:
            answer += 1*(n-i)
            BB = pickups[-i-1] - cap
            pickups[-i-1] = 0
            pickups[-i-2] += BB
    return answer
"""

def solution(cap, n, deliveries, pickups):
    answer, dcap, pcap = 0, 0, 0

    for i in range(n - 1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            tmp = 0
            while dcap < deliveries[i] or pcap < pickups[i]:
                tmp += 1
                dcap += cap
                pcap += cap
            dcap -= deliveries[i]
            pcap -= pickups[i]
            answer += ((i + 1) * tmp * 2)

    return answer

        