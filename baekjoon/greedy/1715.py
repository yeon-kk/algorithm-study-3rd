import sys, heapq
N=int(sys.stdin.readline().rstrip())
q = []
answer = 0
for _ in range(N):
    elem = int(sys.stdin.readline().rstrip())
    heapq.heappush(q,elem)
while len(q)>1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    answer += x+y
    heapq.heappush(q,x+y)
print(answer)
