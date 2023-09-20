import sys
N, M = map(int,sys.stdin.readline().split())
basket = []
for _ in range(N):
    basket.append(list(map(int,sys.stdin.readline().split())))
d = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
cloud=[(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
fourDirections = [(-1,-1),(-1,1),(1,-1),(1,1)]
def cloudMove(cloud, i):
    global visit, basket, d
    tmp = []
    for y,x in cloud:
        ny = (d[i][0]*s + y)%N
        nx = (d[i][1]*s + x)%N
        basket[ny][nx] += 1
        visit[ny][nx]=True
        tmp.append((ny,nx))
    return tmp

def getWater(cloud):
    global fourDirections, basket, N
    for y,x in cloud:
        for dy,dx in fourDirections:
            ny,nx = dy+y,dx+x 
            if ny<0 or N<=ny or nx<0 or N<=nx: continue
            if basket[ny][nx] >0: basket[y][x]+=1

for idx in range(M):
    i, s = map(int,sys.stdin.readline().split())
    i-=1
    visit = [[False]*N for _ in range(N)]
    cloud = cloudMove(cloud, i)
    getWater(cloud)
    cloud.clear()
    for row in range(N):
        for col in range(N):
            if basket[row][col] >1:
                if visit[row][col] : continue
                basket[row][col] -= 2
                cloud.append((row,col))
answer = 0
for elem in basket:
    answer += sum(elem)
print(answer)