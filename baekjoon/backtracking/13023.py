import sys
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
friends = []
found = False
visit = [False for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def backtracking(current):
    global friends, graph, found
    if len(friends) == 5:
        found = True
        return
    for friend in graph[current]:
        if visit[friend]: continue
        friends.append(friend)
        visit[friend]=True
        backtracking(friend)
        friends.pop()
        visit[friend]=False

for i in range(1,N+1):
    friends = []
    visit[i]=True
    friends.append(i)
    backtracking(i)
    friends.pop()
    visit[i]=False
    if found: break
if found:
    print(1)
else:
    print(0)