import copy
def check4Blocks(arr,row,col):
    if arr[row][col] == arr[row][col+1]:
        if col < len(arr[row+1])-1 and arr[row][col+1] == arr[row+1][col] == arr[row+1][col+1]:
            return True
    return False

def remove(arr,removeIdxArr):
    copyArr = copy.copy(arr)    
    removeIdxArr.sort(key=lambda x:(x[0],-x[1]))
    for r,c in removeIdxArr:
        copyArr[r].pop(c)
    return copyArr
    
def searchBoard(arr): # 바뀐 arr
    removeIdxSet = set()
    removeIdxArr = []
    for r in range(len(arr)-1):
        for c in range(len(arr[r])-1):
            if check4Blocks(arr,r,c):
                removeIdxSet.add((r,c))
                removeIdxSet.add((r+1,c))
                removeIdxSet.add((r,c+1))
                removeIdxSet.add((r+1,c+1))
    for item in removeIdxSet:
        removeIdxArr.append(item)
    return removeIdxArr
        

def solution(m, n, board): #m 높이, n 너비 -> n: row, m: col
    createArr = [ list(b) for b in board]
    nBoard = []
    answer = 0
    for col in zip(*createArr[::-1]):
        nBoard.append(list(col))
    
    while True:
        removeIdxArr=searchBoard(nBoard)
        answer += len(removeIdxArr)
        if len(removeIdxArr)==0:
            break
        nBoard=remove(nBoard,removeIdxArr)
    return answer