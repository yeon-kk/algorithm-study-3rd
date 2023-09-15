import sys
C = int(sys.stdin.readline().rstrip())
total = 0
def backtracking(team,position,idx,ablilitySum):
    global total
    if idx == 11:
        total=max(total,ablilitySum)
        return
    for p, score in enumerate(team[idx]):
        if score==0:
            continue
        if position[p]:
            continue
        position[p]=True
        backtracking(team,position,idx+1,ablilitySum+score)
        position[p]=False

for _ in range(C):
    team=[]
    total = 0
    position= {i:False for i in range(11)}
    for _ in range(11):
        team.append(list(map(int,sys.stdin.readline().split())))
    backtracking(team,position,0,0)
    print(total)