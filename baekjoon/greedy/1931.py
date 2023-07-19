# 회의실 배정
# 몇가지를 가정했다.
# 1. 모든 내용들을 먼저 배열에 하나씩 추가한다 => [...불가능] 시간복잡도를 생각해도 어렵다. 
# 2. 하나씩 배열에 추가한다 => 추가하는 기준 필요
# 2-(1) [정렬]: 시작 시간 기준? 종료 시간 기준? 
# 2-(2) 시작 시간 기준: 4가지 경우
# a. --=== [1,5] [3,5] : 대체
# b. ---==_ [1,5] [4,6] : X 
# c. -===-  [1,5] [2,4] : 대체
# d. ----- --- [1,5] [7,9] : 추가

# b처럼 겹친다면 하나를 포기해야 하는데, 종료시간이 더 짧은 것을 택하는게 그리디. 
# 왜냐면 어차피 대체되기 때문에 둘중 하나는 무조건 포함해야 한다. 그렇다면 종료 시간이 더 짧은 것(이미 포함된 것)을 선택하는게 좋다.

# 실패하고 문제를 곰곰히 읽었는데, 놓칠만한 부분은 시작과 끝 지점이 같다는 조건
# a 조건처럼 새로운 회의로 대체하지 않아도 갯수는 동일하다. 
# 하지만 등호 조건이 들어가면 문제에서 시작 시간과 종료 시간이 같은 회의도 대체되어 버린다.

# 초기 조건문은 if end<= beforeEnd 였기 때문에 
# [3,4][4,4] 인 경우 [3,4]가 없어지고 [4,4]가 대체되었다.
# 따라서, 둘 다 포함되어야 하기 때문에 if end<beforeEnd로 수정

N=int(input())
timeTable = []
for _ in range(N):
    start,end = input().split()
    timeTable.append([int(start),int(end)])
timeTable.sort(key=lambda x:(x[0],x[1]))
start,end=timeTable[0][0],timeTable[0][1]
result = [[start,end]]
for start,end in timeTable[1:]:
     beforeStart, beforeEnd = result[-1][0],result[-1][1]
     if end < beforeEnd:
        result[-1][0], result[-1][1] = start, end
     else:
         if beforeEnd <= start:
             result.append([start,end])
print(len(result))