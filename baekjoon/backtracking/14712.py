import sys
N, M = map(int,sys.stdin.readline().split())
totalCount = 0
answer = 0
board = [[0]*M for _ in range(N)]
def isFourBolcks(x,y):
    global board, N
    if 0<x<M and 0<y<N:
        if board[y][x-1] == 1 and board[y-1][x-1] == 1 and board[y-1][x] == 1:
            return True
    return False
def createBoard(cnt):
    global N, M, board, answer
    if cnt == N*M:
        answer += 1
        return
    x,y=cnt//N,cnt%N
    createBoard(cnt+1)
    if not isFourBolcks(x,y):
        board[y][x]=1
        createBoard(cnt+1)
        board[y][x]=0
createBoard(0)
print(answer)