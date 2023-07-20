# 달팽이
# 좌,하,우,상 반복 및 인덱스 조절
N=int(input())
targetNum = int(input())
x = [ [0]*N for _ in range(N)]

currentNum = N*N
round = 0
def printResult (x,targetNum):
    result = []
    for row in range(N):
        print(' '.join(x[row]))
        for col in range(N):
            if x[row][col] == str(targetNum):
                result.append(str(row+1))
                result.append(str(col+1))
    print(' '.join(result))

for n in range(N,-1,-2):
    for i in range(n-1):
        x[i+round][round] = str(currentNum)
        currentNum -= 1
    for i in range(n-1):
        x[N-1-round][i+round] = str(currentNum)
        currentNum -= 1
    for i in range(n-1):
        x[N-1-round-i][N-1-round] = str(currentNum)
        currentNum -= 1
    for i in range(n-1):
        x[round][N-1-round-i] = str(currentNum)
        currentNum -= 1
    round += 1

x[N//2][N//2]= '1'
printResult(x,targetNum)