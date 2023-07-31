# 배열 전체를 돌리는게 아니라, 
# 배열 전체에서 봤을 때 대각선 2개와 가운데 열 1개 가운데 행1개, 총 4개만 돌리게 된다.
# 따라서 가운데 행, 가운데 열이 만나는 지점(arr[n//2][n//2])을 기준으로
# 8개의 원소가 회전하게 된다.(arr[n//2][n//2]인 경우 1개)
# 회전할 겉 배열 arr의 원소를 tmp에 8개 저장 후
# 회전한 각의 음수만큼 시작 인덱스를 정하고 +1을 해서 겉 배열 시작지점(좌측 상단)부터) tmp를 삽입한다.
# 예를들어 45도 회전한 경우, tmp의 시작 인덱스는 1이 아니라 -1이 된다)
# 가운데 행, 가운데 열이 만나는 지점(arr[n//2][n//2])은 회전하지 않기 때문에 제외한다
# 회전각이 0인 경우 함수를 호출하지 않고 그대로 출력한다.
T = int(input())
def createArr(arr,idx,midIdx,lastIdx):
    tmp = []
    tmp.append(arr[idx][idx])
    tmp.append(arr[idx][midIdx])
    tmp.append(arr[idx][lastIdx])
    tmp.append(arr[midIdx][lastIdx])
    tmp.append(arr[lastIdx][lastIdx])
    tmp.append(arr[lastIdx][midIdx])
    tmp.append(arr[lastIdx][idx])
    tmp.append(arr[midIdx][idx])
    return tmp
def insertArr(arr,tmp,idx,midIdx,lastIdx,d):
    arr[idx][idx] = tmp[d%8]
    d += 1
    arr[idx][midIdx] = tmp[d%8]
    d += 1
    arr[idx][lastIdx] = tmp[d%8]
    d += 1
    arr[midIdx][lastIdx] = tmp[d%8]
    d += 1
    arr[lastIdx][lastIdx] = tmp[d%8]
    d += 1
    arr[lastIdx][midIdx] = tmp[d%8]
    d += 1
    arr[lastIdx][idx] = tmp[d%8]
    d += 1
    arr[midIdx][idx] = tmp[d%8]
    return arr

for _ in range(T):
    n,d = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(str,input().split())))
    idx = 0
    midIdx = n//2
    d //= 45
    if d != 0:
        for lastIdx in range(n-1,n//2,-1):
            tmp = createArr(arr,idx,midIdx,lastIdx)
            arr=insertArr(arr,tmp,idx,midIdx,lastIdx,-d)
            idx += 1
    for row in arr:
        print(' '.join(row))
