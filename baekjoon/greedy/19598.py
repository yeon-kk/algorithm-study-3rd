# 최소 회의실 개수
# 1. 배열안에 배열, 2차원 배열
# 2. 배열 안에 종료시간, 1차원 배열
# 3. 가장 작은 종료 시간을 알아야 하는데, 회의가 계속 추가되면 그걸 탐색하는데 시간이 또 필요하다.
# 4. 선형 탐색, 이진탐색, 우선순위 큐를 순서대로 생각해봤고 가장 작은 회의 시간만 찾으면 되기 때문에
#  우선순위 큐를 선택했다.
import heapq
N=int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[0],x[1]))

heap = []
heapq.heappush(heap,arr[0][1])

for start, end in arr[1:]:
    minLast=heapq.heappop(heap)
    if minLast <= start:
        heapq.heappush(heap,end)
    else:
        heapq.heappush(heap,minLast)
        heapq.heappush(heap, end)
print(len(heap))