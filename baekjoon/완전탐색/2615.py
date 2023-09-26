import sys
from collections import deque
N = 19
arr= [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
directions = [(1,0),(1,1),(0,1),(-1,1)]
def search(startY,startX,color,i):
    global arr, visit
    count = 1
    q = deque([(startY,startX,count)])
    while q:
        y,x,count=q.popleft()
        dy,dx = directions[i]
        ny,nx = dy+y, dx+x
        if ny<0 or ny>=N or nx<0 or nx>=N : continue
        if arr[ny][nx] == color:
            q.append((ny,nx,count+1))
    return count
answer = False
for col in range(N):
    for row in range(N):
        color = arr[row][col]
        if color==0: continue
        for i in range(4):
            ny, nx = row-directions[i][0],col-directions[i][1]
            if 0<=ny<N and 0<=nx<N:
                if color == arr[ny][nx]: continue
            count = search(row,col,color,i)
            if count == 5:
                answer = True
                print(color)
                print(row+1,col+1)
                break
    if answer:
        break
if answer == False :print(0)