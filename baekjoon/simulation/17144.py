import sys
R,C,T = map(int,sys.stdin.readline().split())
arr = []
for _ in range(R):
    arr.append(list(map(int,sys.stdin.readline().split())))
cleanerDirection = []
for r in range(R):
    if arr[r][0]==-1:
        cleanerDirection.append(r)
def spread():
    global arr
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    remain = [[0 for _ in range(C)] for _ in range(R)]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    for row in range(R):
        for col in range(C):
            if arr[row][col]==0 or arr[row][col]==-1: continue
            count = 0
            for dy,dx in direction:
                ny, nx = row+dy, col+dx
                if ny<0 or R<=ny or nx<0 or C<=nx: continue
                if arr[ny][nx] == -1: continue
                count += 1
                tmp[ny][nx] += arr[row][col]//5
            remain[row][col] = arr[row][col] - ((arr[row][col]//5)*(count))
    for row in range(R):
        for col in range(C):
            remain[row][col] += tmp[row][col]
    for row in range(R):
        if arr[row][0] == -1:
            remain[row][0] = -1
    return remain

def move(remain,tmp,d):
    global cleanerDirection, C, R
    rowLocation = cleanerDirection[d]
    direction, end, start = 0, 0, 0
    if d == 0: direction, end, start= -1, -1, 1
    else: direction, end, start= 1, R, R-2
    index = 0
    for col in range(1,C):
        remain[rowLocation][col] = tmp[index]
        index+= 1
    for row in range(rowLocation+direction,end,direction):
        remain[row][C-1] = tmp[index]
        index+=1
    for col in range(C-2,-1,-1):
        remain[end-direction][col] = tmp[index]
        index+=1
    for row in range(start,rowLocation,-direction):
        remain[row][0] = tmp[index]
        index+=1
    return remain

def dust(d):
    global cleanerDirection, C, R, arr
    rowLocation = cleanerDirection[d]
    direction, end = 0, 0
    if d == 0: direction, end, start= -1, -1, 1
    else: direction, end, start= 1, R, R-2
    tmp = [0]
    for col in range(1,C):
        tmp.append(arr[rowLocation][col])
    for row in range(rowLocation+direction,end,direction):
        tmp.append(arr[row][C-1])
    for col in range(C-2,-1,-1):
        tmp.append(arr[end-direction][col])
    for row in range(start,rowLocation+direction,-direction):
        tmp.append(arr[row][0])
    tmp.append(-1)
    return tmp

def clean(remain):
    global cleanerDirection, C, R
    up=dust(0)
    down=dust(1)
    remain = move(remain,up,0)
    remain = move(remain,down,1)
    return remain

while T>0:
    arr=spread()
    arr=clean(arr)
    T-=1
answer = 2
for row in range(R):
    for col in range(C):
        answer += arr[row][col]
print(answer)