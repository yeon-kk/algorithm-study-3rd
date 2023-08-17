import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
pArr, mArr = [],[]
for elem in arr:
    if elem<0:
        mArr.append(elem)
    else:
        pArr.append(elem)
pArr.sort()
mArr.sort(key=lambda x:-x)
if len(pArr) ==0 :
    print(mArr[1],mArr[0])
elif len(mArr)==0:
    print(pArr[0],pArr[1])
else:
    minResult = int(1e9)
    result1, result2 = 0 , 0
    curArr = pArr if len(pArr)<len(mArr) else mArr
    compArr = mArr if len(pArr)<len(mArr) else pArr
    if len(curArr) >=2 and minResult > abs(curArr[0]+ curArr[1]): 
        result1, result2 = curArr[0], curArr[1]
        minResult = abs(result1 + result2)
    if len(compArr) >=2 and minResult > abs(compArr[0]+ compArr[1]):
        result1, result2 = compArr[0], compArr[1]
        minResult = abs(result1 + result2)
    for elem in curArr:
        start, end = 0, len(compArr)-1
        while start <= end:
            mid = (start + end)//2
            if minResult > abs(compArr[mid]+elem):
                minResult = abs(compArr[mid]+elem)
                result1, result2 = compArr[mid], elem
            if abs(compArr[mid]) < abs(elem):
                start = mid + 1
            elif abs(compArr[mid]) == abs(elem):
                break
            else:
                end = mid - 1
        if minResult ==0: break       
    print(min(result1,result2),max(result1,result2))
