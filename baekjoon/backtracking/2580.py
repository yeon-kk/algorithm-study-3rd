import sys
arr = []
for _ in range(9):
    arr.append(list(map(int,sys.stdin.readline().split())))
zero = []
for row in range(9):
    for col in range(9):
        if arr[row][col]==0:
            zero.append((row,col))
def checkNum(row,col,item):
    global arr
    searchRow, searchCol = (row//3)*3, (col//3)*3    
    if item in [ arr[r][col] for r in range(9)]: return False
    
    if item in arr[row]: return False
    
    for r in range(searchRow,searchRow+3):
        for c in range(searchCol,searchCol+3):
            if item == arr[r][c]: return False
    return True
completed = False
def backtracking(idx):
    global arr, zero, completed
    if completed: return
    if idx == len(zero):
        completed = True
        for i in range(9):
            print(*arr[i])
        return
    row,col=zero[idx]
    for item in range(1,10):
        if checkNum(row,col,item):
            arr[row][col] = item
            backtracking(idx+1)
            arr[row][col] = 0

backtracking(0)