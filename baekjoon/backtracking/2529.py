import sys
N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().split())

answer = []
visit = {}
maxResult = 0
minResult = 9999999999
for i in range(10):
    visit[i]= False
def check(left,right,op):
    if op == '<':
        if left < right:
            return True
        else:
            return False
    else:
        if left > right:
            return True
        else:
            return False

def backtracking(numbers):
    global visit, arr, N, result, minResult ,maxResult
    if N+1 == len(numbers):
        tmp = ''.join([str(num) for num in numbers])
        minResult = min(int(tmp),minResult)
        maxResult = max(int(tmp),maxResult)
        return
    for i in range(10):
        if visit[i]:
            continue
        if not check(numbers[-1],i,arr[len(numbers)-1]):
            continue
        visit[i]=True
        numbers.append(i)
        backtracking(numbers)
        numbers.pop()
        visit[i]=False
for i in range(10):
    visit[i]=True
    backtracking([i])
    visit[i]=False
print(str(maxResult).zfill(N+1))
print(str(minResult).zfill(N+1))