import sys
from collections import deque
N= int(sys.stdin.readline())
parentnodeList = list(map(int,sys.stdin.readline().split()))
deleteNode = int(sys.stdin.readline())
deleteNodeParent = -1
tree = {}
for node in range(N):
    tree[node] = []
for childnode in range(N):
    if parentnodeList[childnode] != -1:
        tree[parentnodeList[childnode]].append(childnode)
    if childnode == deleteNode:
        deleteNodeParent = parentnodeList[childnode]

q = deque([deleteNode])
while q:
    node = q.popleft()
    for child in tree[node]:
        q.append(child)
    tree.pop(node)
if deleteNodeParent != -1:
    tree[deleteNodeParent].remove(deleteNode)
leafnodeCount = 0
for parentnode in range(N):
    child=tree.get(parentnode,-1)
    if child!=-1 and len(child)==0:
        leafnodeCount+=1
print(leafnodeCount)