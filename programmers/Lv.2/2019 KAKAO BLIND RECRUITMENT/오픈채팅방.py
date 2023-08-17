def solution(record):
    users = {}
    answer = []
    for fullInfo in record:
        info = fullInfo.split()
        op,uid,nickname = info[0], info[1], '' if len(info)==2 else info[2]
        if op == 'Enter' or op == 'Change':
            users[uid] = nickname
    for fullInfo in record:
        info = fullInfo.split()
        op,uid = info[0], info[1]
        if op == 'Change': continue
        message = users[uid]+'님이 '
        if op == 'Enter':
            message += '들어왔습니다.'
        elif op == 'Leave':
            message += '나갔습니다.'
        answer.append(message)
    return answer