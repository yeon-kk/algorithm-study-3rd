import sys
from collections import deque
N = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(edges):
    s, e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
visit = [ False for _ in range(N+1)]
def bfs(start):
    q = deque([start])
    visit[start]=True
    count = 0
    while q:
        x=q.popleft()
        for child in graph[x]:
            if visit[child]:
                continue
            visit[child]=True
            count +=1
            q.append(child)
    return count
print(bfs(1))