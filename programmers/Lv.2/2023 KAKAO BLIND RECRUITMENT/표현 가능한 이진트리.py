def solution(numbers):
    answer = []
    length = [ 2**i for i in range(6)]
    totalNodeCnt = [ sum(length[:i+1]) for i in range(6)]
    for n in numbers:
        result = []
        num = list(bin(n)[2:])
        curLen = len(num)
        targetLen = 1
        for a,b in zip(totalNodeCnt,totalNodeCnt[1:]):
            if a< curLen <=b: targetLen = b
        arr=list(''.join(num).zfill(targetLen))
        i = 0
        if len(arr)==1:
            arr[i]
            i+=1
            answer.append(1)
        isCheck = False
        while len(arr)>i+2:
            if isCheck: break
            while len(arr)>i+2:
                left=arr[i]
                parent=arr[i+1]
                right=arr[i+2]
                i += 3
                if left=='1' or right=='1': 
                    if parent=='0': 
                        answer.append(0)
                        isCheck = True
                        break
                result.append(parent)
                if len(arr)>i: 
                    tmp = arr[i]
                    i+=1
                    result.append(tmp)
                if len(arr)>=i and len(result)==1:
                    answer.append(1)
                    break
            arr = result
            result=[]
            i=0
    return answer