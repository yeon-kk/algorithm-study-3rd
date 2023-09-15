def solution(s):
    answer = []
    obj = {}
    max_len = 0
    for elem in list(s[2:-2].split('},{')):
        arr = list(elem.split(','))
        obj[len(arr)] = arr
        max_len = max(max_len,len(arr))
    visit = {}
    for elem in obj[max_len]:
        visit[elem] = False
    for idx in range(1,max_len+1):
        for elem in obj[idx]:
            if visit[elem]: continue
            visit[elem] = True
            answer.append(int(elem))
    
    return answer