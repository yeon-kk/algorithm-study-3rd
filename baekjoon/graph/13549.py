from collections import deque
N, K = map(int,input().split())
count = [ 0 for _ in range(200001)]
visit = [ False for _ in range(200001)]
q = deque([N])
visit[N] = True

while q:
    x=q.popleft()
    if 0< x*2 <= 200000 and not visit[x*2]:
        count[x*2] = count[x]
        q.appendleft(x*2)
        visit[x*2] = True

    if x-1 >= 0 and not visit[x-1] : 
        count[x-1] = count[x]+1
        visit[x-1] = True
        q.append(x-1)

    if x+1 <= K and not visit[x+1]: 
        count[x+1] = count[x]+1
        visit[x+1] = True
        q.append(x+1)
print(count[K])