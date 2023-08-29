import sys
from collections import deque
from collections import Counter
N,M,K,X = map(int,sys.stdin.readline().split())
graph = {}
for idx in range(N+1):
    graph[idx] = []
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
def bfs(start):
    global graph,N
    distance = [int(1e9) for _ in range(N+1)]
    distance[start]=0
    q=deque([(start,1)])
    while q:
        x,cost = q.popleft()
        for destination in graph[x]:
            if cost < distance[destination]:
                distance[destination] = cost
                q.append((destination,cost+1))
    return distance
dist =bfs(X)
notExist = True
for idx, elem in enumerate(dist):
    if elem == K:
        notExist = False
        print(idx)
if(notExist):
    print(-1)