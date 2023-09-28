from collections import deque
import sys
N, L, R = map(int,sys.stdin.readline().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
directions=[(-1,0),(1,0),(0,1),(0,-1)]
def search(startY, startX, visit):
    global arr,N, directions,L,R
    count=0
    q= deque([(startY,startX)])
    visit[startY][startX]=True
    city=[]
    while q:
        y,x= q.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if ny<0 or ny>=N or nx <0 or nx>=N: continue
            if visit[ny][nx]: continue
            if abs(arr[ny][nx]-arr[y][x])<L or abs(arr[ny][nx]-arr[y][x])>R : continue
            visit[ny][nx]=True
            q.append((ny,nx))
            count+=arr[ny][nx]
            city.append((ny,nx))
    if city: 
        city.append((startY,startX))
        count += arr[startY][startX]
        return count, visit, city
    else:
        return 0, visit, city
def moving(city,average):
    global arr, N
    for y,x in city:
        arr[y][x] = average
answer = 0
for i in range(2000):
    total = 0
    visit=[[False]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visit[row][col]: continue
            count, visit, city = search(row,col, visit)
            if count != 0:
                average = count//len(city)
                moving(city,average)
            total += count
    if total == 0: break
    answer += 1
print(answer)