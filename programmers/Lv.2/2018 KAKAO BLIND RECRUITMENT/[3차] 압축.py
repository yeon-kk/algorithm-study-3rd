def solution(msg):
    answer = []
    dictionary = {}
    msgLen = len(msg)
    for idx, elem in enumerate(range(65,91)):
        dictionary[chr(elem)] = idx+1
    idx = 0
    while idx < msgLen:
        tmp = msg[idx]
        nextIdx = 0
        while tmp in dictionary:
            nextIdx+=1
            if idx+nextIdx < msgLen:
                tmp+=msg[idx+nextIdx]
            else: break
        if tmp in dictionary:
            answer.append(dictionary[tmp])
            idx += 1
        else:
            answer.append(dictionary[tmp[:-1]])
            dictionary[tmp] = len(dictionary)+1
        idx += nextIdx
    return answer