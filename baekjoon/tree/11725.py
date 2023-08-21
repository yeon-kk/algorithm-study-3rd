import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [ [] for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int,sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

dictionary = {}
def bfs(start):
    global arr
    tree = {}
    visit = [ False for _ in range(N+1)]
    visit[start] = True
    q=deque([start])
    while q:
        parent=q.popleft()
        for child in arr[parent]:
            if visit[child]!=True:
                q.append(child)
                visit[child]= True
                tree[child]=parent
    return tree
tree=bfs(1)
for node in range(2,N+1):
    print(tree[node])