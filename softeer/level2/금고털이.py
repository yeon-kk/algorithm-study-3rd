# 무게당 가격으로 먼저 정렬한 뒤, 순차적으로 무게를 추출한다

import sys
W,N=map(int,sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    m,p=map(int,sys.stdin.readline().rstrip().split())
    arr.append((m,p))
arr.sort(key=lambda x:-x[1])
price = 0
for m,p in arr:
    if W >= m:
        W-=m
        price += (m*p)
    else:
        price += (W*p)
        break

print(price)