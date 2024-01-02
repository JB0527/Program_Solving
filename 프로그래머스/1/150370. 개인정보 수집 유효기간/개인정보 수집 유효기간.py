def compare(contract_date, today):
    if contract_date[0] > today[0]:
        return True
    elif contract_date[0] == today[0] and contract_date[1] > today[1]:
        return True
    elif contract_date[0] == today[0] and contract_date[1] == today[1] and contract_date[2] > today[2]:
        return True
    
    return False

def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    contract = {term[0]:int(term[2:]) for term in terms }
    num = 1
    
    for i in privacies:
        temp = i.split(' ')
        date = list(map(int,temp[0].split('.')))
        date[1] += contract[temp[1]]
        
        if date[1] > 12 : #오버하는 경우 년도를
            if date[1] % 12 == 0: #12배수인경우 월별로는 고정값만들기 
                date[0] += (date[1] // 12) -1
                date[1] = 12
            else: #12배수가 아니라면
                date[0] += (date[1] // 12)
                date[1] %= 12
        
        if compare(date, today) == False:
            answer.append(num)
        num += 1
    return answer