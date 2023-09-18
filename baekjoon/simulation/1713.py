import sys
N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
answer = []
student = { idx:0 for idx in range(1,101) }
for idx in range(M):
    recommended = arr[idx]
    if student[recommended] != 0:
        student[recommended] += 1
    else:
        minValue, index, k = 1001, -1, 0
        if len(answer)==N:
            for i,key in enumerate(answer):
                if minValue> student[key]:
                    minValue = student[key]
                    k = key
                    index = i
            student[k]=0
            answer.pop(index)
            student[recommended]=1
            answer.append(recommended)
        else:
            answer.append(recommended)
            student[recommended]=1
answer.sort()
print(*answer)