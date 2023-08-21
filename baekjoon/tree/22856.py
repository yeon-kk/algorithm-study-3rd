import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    parent, leftChild, rightChild = map(int,sys.stdin.readline().split())
    tree[parent] = [leftChild,rightChild]
cnt = 0
visit = set()
def isAllVisited(): 
    global visit, N
    return True if len(visit)==N else False
def dfs(parent):
    global tree, cnt, visit
    for child in tree[parent]:
        if child != -1:
            cnt +=1
            dfs(child)
            if isAllVisited() == False:
                cnt += 1
        visit.add(parent)
dfs(1)
print(cnt)