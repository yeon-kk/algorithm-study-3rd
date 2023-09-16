import sys
N = int(sys.stdin.readline().rstrip())
count = -1
answer = False
arr = []
def backtracking(numbers,target):
    global N, count, answer
    if len(numbers) == target:
        count+=1
        tmp = 0
        for idx, num in enumerate(numbers[::-1]):
            tmp += (10**(idx))*num
        arr.append(tmp)
        if count == N:            
            answer = True
        return
    lastWord = numbers[-1]
    for num in range(lastWord-1,-1,-1):
        numbers.append(num)
        backtracking(numbers,target)
        numbers.pop()
def start():
    for target in range(1,11):
        for n in range(0,10):
            backtracking([n],target)
            if answer:
                return
start()
arr.sort()
print(arr[N] if N < len(arr) else -1)