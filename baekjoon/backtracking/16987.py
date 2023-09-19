import sys
N = int(sys.stdin.readline().rstrip())
eggs = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = 0

def isAllBroken(cur):
    global eggs
    for idx, [elem, _] in enumerate(eggs):
        if cur == idx: continue
        if elem > 0:
            return False
    return True

def backtracking(cur):
    global eggs, answer
    while cur<N and eggs[cur][0]<=0:
        cur+=1
    if cur==N or isAllBroken(cur):
        tmp = 0
        for elem, _ in eggs:
            if elem >0: continue
            tmp+=1
        answer=max(answer,tmp)
        return
    for i in range(N):
        if i == cur: continue
        if eggs[i][0]<=0: continue
        a, b = eggs[i][1], eggs[cur][1]
        eggs[cur][0] -= a
        eggs[i][0] -= b
        backtracking(cur+1)
        eggs[cur][0] += a
        eggs[i][0] += b

backtracking(0)
print(answer)