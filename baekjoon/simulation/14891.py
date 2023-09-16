import sys
from collections import deque
arr = []
for _ in range(4):
    arr.append(deque(list(map(int,sys.stdin.readline().rstrip()))))
K = int(sys.stdin.readline().rstrip())
indicator = []
for _ in range(K):
    num,direction = map(int,sys.stdin.readline().split())
    num -= 1
    rIdx, rDir = num+1, direction
    lIdx, lDir = num-1, direction
    right = arr[num][2]
    left = arr[num][6]
    if direction == 1:
        last=arr[num].pop()
        arr[num].appendleft(last)        
    else:
        last = arr[num].popleft()
        arr[num].append(last)
    while rIdx<4:
        if right != arr[rIdx][6] :
            right = arr[rIdx][2]
            if rDir == 1:
                last=arr[rIdx].popleft()
                arr[rIdx].append(last)
            else:
                last=arr[rIdx].pop()
                arr[rIdx].appendleft(last)
            rDir *= -1
        else: break
        rIdx+=1
    while lIdx>-1:
        if arr[lIdx][2] != left :
            left = arr[lIdx][6]
            if lDir == 1:
                last=arr[lIdx].popleft()
                arr[lIdx].append(last)
            else:
                last=arr[lIdx].pop()
                arr[lIdx].appendleft(last)
            lDir *= -1
        else: break
        lIdx-=1
answer = 0
for idx in range(4):
    if arr[idx][0] == 1:
        answer += 2**(idx)
print(answer)
