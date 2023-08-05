# 제약 조건이 100,000이었기 때문에 정렬 시간초과에 주의해야 하는 문제였다고 생각한다.
# 그리고 입력받는 N과 반복문 횟수를 착각하지 않도록 해야 하는데, 꼭 테스트 케이스로 예외적인 상황을 만들어보자.
# rank로 순위를 담는 변수는 동점으로 같은 등수를 표기하기 위한 변수이며
# people은 동점이 아닐 때, 해당 참가자보다 앞선 사람의 수를 표기하기 위한 변수로 사용했다.
# heapq로 배열에 삽입과 동시에 정렬하여 정렬에 시간을 단축
# 최대힙을 구현하기 위해 heapq에 삽입하는 값에 음수를 곱해주었다.
# 뿐만 아니라 index(참가자 번호)로 같이 쌍으로 삽입하여, 삽입된 요소는 (-value,index)의 형태이다

import sys
import heapq
N=int(sys.stdin.readline().rstrip())

def makeRank(queue):
    global N
    rank = 1
    beforeScore = 1001
    ranks = [ 0 for _ in range(N)]
    people = 0
    while queue:
        score,index =heapq.heappop(queue)
        people += 1
        score = -score
        if beforeScore == score:
            ranks[index] = str(rank)
        else:
            ranks[index] = str(people)
            rank = people
        beforeScore = score
    print(' '.join(ranks))

scores = []
for _ in range(3):
    queue = []
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    scores.append(li)
    for idx,score in enumerate(li):
        heapq.heappush(queue,(-score,idx))
    makeRank(queue)

totalQueue = []
for index, score in enumerate(zip(*scores)):
    heapq.heappush(totalQueue,(-sum(score),index))

makeRank(totalQueue)
