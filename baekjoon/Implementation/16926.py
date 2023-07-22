# 배열 돌리기 1
# 배열을 돌리는 방법 고민
# 1. 좌,하 => row 또는 col 증가 / 우,상 => row 또는 col 감소
# (1) arr[i+k][j+l] = arr[i][j] .. 
# : 시작 지점에 따라 증가와 감소를 따로 계산하는건 복잡하다
# 2. 테두리 하나만 놓고 생각한다.
# (1) 테두리 하나를 1차원 배열에 담고
# (2) 좌측 상단부터 채우는 것으로 한다.
# (3) 회전을 완료한 시점에 넣어야 할 원소를 시작 위치부터 채운다
# 기능: 테두리 배열 추출, 회전 수(나머지 이용),배열 삽입
# 엣지 케이스를 먼저 생각해보자.
N,M,R = map(int, input().split())
x=[]
for _ in range(N):
    x.append(list( input().split()))

def getOutlineM1(x, n,startRow,startCol):
    result = []
    row, col = startRow, startCol+1
    for _ in range(0, n, 1):
        result.append(x[row][col])
        row += 1
    return result

def getOutline(x, m,n,startRow,startCol):
    result = []
    row, col = startRow, startCol
    for _ in range(0, m, 1):
        col += 1
        result.append(x[row][col])
    if n == 1:
        return result
    for _ in range(1, n, 1):
        row += 1
        result.append(x[row][col])
    for _ in range(1, m, 1):
        col -= 1
        result.append(x[row][col])
    for _ in range(1, n - 1, 1):
        row -= 1
        result.append(x[row][col])
    return result

def setOutlineM1(x, n,startRow,startCol, items, startIdx):
    itemLength = len(items)
    startIdx %= itemLength
    row, col = startRow, startCol +1

    for _ in range(0, n, 1):
        x[row][col] = items[startIdx]
        startIdx = (startIdx+1) % itemLength
        row += 1
    return x


def setOutline(x, m,n,startRow,startCol, items, startIdx):
    itemLength = len(items)
    startIdx %= itemLength
    row, col = startRow, startCol
    for _ in range(0, m, 1):
        col += 1
        x[row][col] = items[startIdx]
        startIdx = (startIdx+1)  % itemLength
    if n == 1:
        return x
    for _ in range(1, n, 1):
        row += 1
        x[row][col] = items[startIdx]
        startIdx = (startIdx+1)  % itemLength
    for _ in range(1, m, 1):
        col -= 1
        x[row][col] = items[startIdx]
        startIdx = (startIdx+1)  % itemLength
    for _ in range(1, n - 1, 1):
        row -= 1
        x[row][col] = items[startIdx]
        startIdx = (startIdx+1)  % itemLength
    return x

if N==1 and M==1:
    print(x[0][0])
else:
    result = []

    startRow, startCol = 0, -1
    for m, n in zip(range(M, -1, -2), range(N, -1, -2)):
        if m*n == 0:
            break
        if m == 1:
            result = getOutlineM1(x, n, startRow, startCol)
        else:
            result = getOutline(x, m, n, startRow, startCol)
        if len(result) == 0: break
        r = R % (m + m + n + n - 4)
        if m == 1:
            x = setOutlineM1(x, n, startRow, startCol, result, r)
        else:
            x = setOutline(x, m, n, startRow, startCol, result, r)
        startRow += 1
        startCol += 1

    for arr in x:
        print(' '.join(arr))